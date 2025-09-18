from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    ROLE_USER = 'User'
    ROLE_TUTOR = 'Tutor'
    ROLE_CHOICE = [
        (ROLE_USER,'User'),
        (ROLE_TUTOR, 'Tutor')
    ]
    
    username = None 
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default=ROLE_USER)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.email} ({self.role})"
    
