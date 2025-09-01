from django.db import models
from django.conf import settings
from services.models import Service

class SpecialistProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="specialist_profile")
    national_code = models.CharField(max_length=10, blank=True)
    national_card_image = models.FileField(upload_to="ids/", null=True, blank=True)
    bank_account_number = models.CharField(max_length=50, blank=True)
    card_number = models.CharField(max_length=16, blank=True)
    shaba = models.CharField(max_length=26, blank=True)
    address = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    is_approved_by_admin = models.BooleanField(default=False)
    cancel_count_daily = models.PositiveIntegerField(default=0)

    services = models.ManyToManyField(Service, through="SpecialistService", related_name="specialists")

class SpecialistService(models.Model):
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    custom_price = models.PositiveIntegerField(null=True, blank=True)
    custom_duration_min = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        unique_together = ("specialist", "service")
