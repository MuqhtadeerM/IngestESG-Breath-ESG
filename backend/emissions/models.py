from django.db import models

# Create your models here.
from organizations.models import Organization
from ingestion.models import RawRecord


class EmissionRecord(models.Model):

    SCOPE_CHOICES = [
        ('SCOPE_1', 'Scope 1'),
        ('SCOPE_2', 'Scope 2'),
        ('SCOPE_3', 'Scope 3'),
    ]

    STATUS_CHOICES = [
        ('PENDING_REVIEW', 'Pending Review'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.SET_NULL,
        null=True
    )

    activity_type = models.CharField(max_length=255)

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    quantity = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_unit = models.CharField(max_length=50)

    co2e_emissions = models.FloatField()

    suspicious_flag = models.BooleanField(default=False)

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='PENDING_REVIEW'
    )

    locked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_type