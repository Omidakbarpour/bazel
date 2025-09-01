from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, VerifyPhoneSerializer, UserSerializer

User = get_user_model()

# Very basic in-memory store for demo purposes (replace with SMS adapter + DB)
SMS_STORE: dict[str, dict] = {}

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        phone = serializer.validated_data["phone"]
        referred_by = serializer.validated_data.get("referred_by")
        user, _ = User.objects.get_or_create(email=email, defaults={"phone": phone})
        user.phone = phone
        if referred_by:
            user.referred_by = referred_by
        user.is_active = True
        user.set_unusable_password()
        user.save()
        import random
        code = f"{random.randint(100000, 999999)}"
        SMS_STORE[phone] = {"code": code, "ts": timezone.now()}
        return Response({"detail": "verification_code_sent", "mock_code": code})

class VerifyPhoneView(generics.GenericAPIView):
    serializer_class = VerifyPhoneSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]
        entry = SMS_STORE.get(phone)
        if not entry or entry["code"] != code:
            return Response({"detail": "invalid_code"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({"detail": "user_not_found"}, status=status.HTTP_404_NOT_FOUND)
        user.is_verified_phone = True
        user.save()
        refresh = RefreshToken.for_user(user)
        return Response({"access": str(refresh.access_token), "refresh": str(refresh)})

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
