from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    assigned_to = models.CharField(max_length=200)

    def __str__(self):
        return self.task_name
