from django.urls import reverse
from django.db import models


class Remember(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    about = models.TextField()
    photo = models.ImageField(upload_to='images',
                              null=True, blank=True)

    def __str__(self):
        return self.last_name

class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title