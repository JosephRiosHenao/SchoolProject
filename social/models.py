from django.db import models

# Create your models here.

class Post(models.Model):
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='posts/photos')
    likes = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name='likes', null=True, blank=True)
    state = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} by @{}'.format(self.title,  self.user.username)