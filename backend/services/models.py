from django.db import models
from django.conf import settings

class ServiceCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services")
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    duration_min = models.PositiveIntegerField(default=60)
    default_price = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.category.name} - {self.name}"
