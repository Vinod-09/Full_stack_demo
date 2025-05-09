from django.db import models
from django.utils import timezone

# Create your models here.
class user_task(models.Model):
    task_title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task_title
