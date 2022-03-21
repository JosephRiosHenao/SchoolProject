from django.contrib.auth.models import User
from django.db import models


GENDERS = [
    ('Masculino','Masculino'),
    ('Femenino','Femenino'),
    ('No binario','No binario'),
]

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    picture = models.ImageField(upload_to='users/pictures', blank=True, 
                                default='users/pictures/default.jpg', null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    organization = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    gender = models.CharField(max_length=15 , choices=GENDERS, blank=True, default='No binario')
    
    def __str__(self):
        return self.user.username