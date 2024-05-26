from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']
    email = models.EmailField(unique=True)

    class Meta:
        ordering = ('email',)

    def __str__(self):
        return self.username
