from django.db import models
from django.contrib.auth.models import AbstractUser



class Human(AbstractUser):
    email = models.EmailField("email address")
    # USERNAME_FIELD = "email"
    # REQUIRED_FIELDS = []
    