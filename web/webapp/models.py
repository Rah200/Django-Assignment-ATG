from django.db import models
from django.db import connections
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    profile_image = models.ImageField(null=True, blank=True)


class Blog(models.Model):
    blog_image = models.ImageField(null=True, blank=True)
    blog_title = models.CharField(max_length=30)
    blog_summary = models.CharField(max_length=50)
    blog_content = models.TextField(max_length=50)

    def __str__(self):
        return self.blog_title
