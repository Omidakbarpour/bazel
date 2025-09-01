from django.db import models
from django.conf import settings
from django.utils import timezone
from specialists.models import SpecialistProfile
from services.models import Service

class Booking(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bookings")
    specialist = models.ForeignKey(SpecialistProfile, on_delete=models.CASCADE, related_name="bookings")
    services = models.ManyToManyField(Service, related_name="bookings")
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    total_price = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def overlaps(self) -> bool:
        qs = Booking.objects.filter(
            specialist=self.specialist,
            status__in=["pending", "confirmed"],
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime,
        )
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        return qs.exists()
