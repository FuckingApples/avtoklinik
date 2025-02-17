from datetime import timedelta

from rest_framework import generics, status
from rest_framework.exceptions import Throttled
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.timezone import now

from apps.api.serializers.otp import VerifyEmailOTPSerializer
from apps.users.models import UserOTP
from apps.users.services.otp import generate_otp, verify_otp, generate_otp_secret


class RequestEmailOTPAPI(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        user = request.user
        last_otp = UserOTP.objects.filter(user=user).first()

        if last_otp and (now() - last_otp.created_at) < timedelta(minutes=5):
            raise Throttled(detail="You can get OTP once per 5 minutes.")

        _, raw_secret = generate_otp_secret()
        email_otp, _ = UserOTP.objects.update_or_create(
            user=user,
            defaults={
                "otp_secret": raw_secret,
                "is_verified": False,
                "created_at": now(),
            },
        )

        otp = generate_otp(raw_secret)

        # TODO: Add email sending functionality
        print(f"OTP for {user.email}: {otp}")

        return Response(
            {"message": "OTP code was sent to email"}, status=status.HTTP_200_OK
        )


class VerifyEmailOTPAPI(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = VerifyEmailOTPSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        otp = serializer.validated_data["otp"]
        user = request.user

        try:
            email_otp = UserOTP.objects.get(user=user)
        except UserOTP.DoesNotExist:
            return Response(
                {"message": "OTP not found"}, status=status.HTTP_404_NOT_FOUND
            )

        if email_otp.is_expired():
            return Response(
                {"message": "OTP expired"}, status=status.HTTP_400_BAD_REQUEST
            )

        if email_otp.is_verified:
            return Response(
                {"message": "OTP was used"}, status=status.HTTP_400_BAD_REQUEST
            )

        if not verify_otp(email_otp.otp_secret, otp, lifetime=email_otp.lifetime):
            return Response(
                {"message": "OTP not valid"}, status=status.HTTP_400_BAD_REQUEST
            )

        email_otp.is_verified = True
        email_otp.save()
        user.is_email_verified = True
        user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
