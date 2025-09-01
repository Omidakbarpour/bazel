from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    phone = serializers.CharField()
    referred_by = serializers.CharField(required=False, allow_null=True, allow_blank=True)

class VerifyPhoneSerializer(serializers.Serializer):
    phone = serializers.CharField()
    code = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone", "role", "referral_code", "referred_by", "is_verified_phone"]
        read_only_fields = ["role", "referral_code", "is_verified_phone"]
