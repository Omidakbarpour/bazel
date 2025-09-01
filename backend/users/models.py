from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("customer", "Customer"),
        ("specialist", "Specialist"),
        ("admin", "Admin"),
    )
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")
    referral_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    referred_by = models.CharField(max_length=6, null=True, blank=True)
    is_verified_phone = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    def save(self, *args, **kwargs):
        if not self.referral_code:
            import random
            self.referral_code = f"{random.randint(0, 999999):06d}"
        super().save(*args, **kwargs)
