from django.db import models

# Create your models here.

from organizations.models import Organization


class DataSource(models.Model):

    SOURCE_TYPES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    file_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    uploaded_by = models.CharField(max_length=255)

    processing_status = models.CharField(
        max_length=50,
        default='PENDING'
    )

    def __str__(self):
        return f"{self.organization.name} - {self.source_type}"



class RawRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('FAILED', 'Failed'),
    ]

    datasource = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE,
        related_name='raw_records'
    )

    row_number = models.IntegerField()

    raw_payload = models.JSONField()

    processing_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    error_message = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Row {self.row_number}"