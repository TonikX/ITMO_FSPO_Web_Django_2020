from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Task(models.Model):
    title=models.CharField('Название', max_length=50)
    task=models.TextField('Описание')

    def __str__(self):
        return self.title



