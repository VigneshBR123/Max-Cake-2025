from django.db import models

from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):

    ADMIN = 'Admin', 'Admin'

    USER = 'User', 'User'

class Profile(AbstractUser):

    role = models.CharField(max_length=20, choices=RoleChoices.choices)

    phone_num = models.CharField(max_length=15, unique=True)

    class Meta:

        verbose_name = 'profile'

        verbose_name_plural = 'profiles'

    def __str__(self):

        return f'{self.username}' 