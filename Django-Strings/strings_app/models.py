from django.db import models


class StringExample(models.Model):
    """Optional persistence layer — save strings used during the presentation."""

    text = models.CharField(max_length=500)
    category = models.CharField(max_length=50, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.text[:50]
