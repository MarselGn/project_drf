from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='номер телефона')
    city = models.CharField(max_length=100, verbose_name='страна')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
