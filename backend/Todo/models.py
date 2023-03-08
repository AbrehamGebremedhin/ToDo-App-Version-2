from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=128)
    task_description = models.TextField()
    task_priority = models.CharField(max_length=32)
    task_endtime = models.DateField()
    task_status = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_title


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=64)
