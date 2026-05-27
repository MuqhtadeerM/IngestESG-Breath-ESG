from django.db import models

# Create your models here.

class AuditLog(models.Model):

    action = models.CharField(max_length=255)

    model_name = models.CharField(max_length=255)

    record_id = models.IntegerField()

    changed_by = models.CharField(max_length=255)

    previous_data = models.JSONField(
        null=True,
        blank=True
    )

    new_data = models.JSONField(
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action