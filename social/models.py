from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)
    
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='posts/photos')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} by @{}'.format(self.title,  self.user.username)