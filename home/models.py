from django.db import models
from django.utils import timezone

class Task(models.Model):
    task = models.CharField(max_length=100)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return 'Task = {}'.format(self.task)