from django.db import models
from django.utils import timezone  # Import timezone

class add(models.Model): 
    task = models.CharField(max_length=15)
    description = models.TextField(max_length=100)
    time = models.DateTimeField(default=timezone.now)  # Corrected

    def __str__(self):
        return self.task
