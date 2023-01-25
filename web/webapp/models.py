from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    profile_image = models.ImageField(upload_to='profileimage', blank=True)
