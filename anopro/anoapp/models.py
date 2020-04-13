from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.urls import reverse


class Fashion(models.Model):
    brand_name = models.CharField(max_length=240)
    product = models.CharField(max_length=240)
    year = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='image_pics/',
            default='image_pics/default.jpg')

    def get_absolute_url(self):
        return reverse('anoapp:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.brand_name












class About(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
