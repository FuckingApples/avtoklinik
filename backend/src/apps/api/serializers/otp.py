from rest_framework import serializers


class VerifyEmailOTPSerializer(serializers.Serializer):
    otp = serializers.CharField()

    def validate_otp(self, otp):
        if not otp.isdigit():
            raise serializers.ValidationError("OTP must be an integer")
        return otp
