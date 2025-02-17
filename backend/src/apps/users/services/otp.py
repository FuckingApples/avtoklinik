import pyotp
from django.contrib.auth.hashers import make_password

OTP_DIGITS = 8
OTP_LIFETIME = 60 * 60 * 12  # 12 hours


def generate_otp_secret():
    raw_secret = pyotp.random_base32()
    return make_password(raw_secret), raw_secret


def generate_otp(otp_secret, digits=OTP_DIGITS, lifetime=OTP_LIFETIME):
    totp = pyotp.TOTP(otp_secret, digits=digits, interval=lifetime)
    return totp.now()


def verify_otp(otp_secret, otp, digits=OTP_DIGITS, lifetime=OTP_LIFETIME):
    totp = pyotp.TOTP(otp_secret, digits=digits, interval=lifetime)
    return totp.verify(otp)
