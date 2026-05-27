from django.db import models

# Create your models here.
from emissions.models import EmissionRecord


class ReviewDecision(models.Model):

    DECISION_CHOICES = [
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    emission_record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    decision = models.CharField(
        max_length=20,
        choices=DECISION_CHOICES
    )

    reviewer_name = models.CharField(max_length=255)

    comments = models.TextField(blank=True)

    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.decision