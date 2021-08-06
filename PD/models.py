from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Patient(models.Model):
        firstname = models.CharField(max_length=100)
        lastname  = models.CharField(max_length=100)
        choose_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        )
        gender = models.CharField( max_length=100,choices=choose_gender)
        age = models.IntegerField(max_length=3,null=True)
        disease  = models.CharField(max_length=100)
        doctor   = models.CharField(max_length=100)
        fees = models.IntegerField(default=500,null=False)
        medsstarted =  models.DateTimeField(default=timezone.now)
    
    
        def __str__(self):
            return self.firstname

        def get_absolute_url(self):
            return reverse("patient-detail", kwargs={"pk": self.pk})
