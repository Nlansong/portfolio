from django.db import models
from taggit.managers import TaggableManager


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    tech_stack = TaggableManager()
    picture = models.ImageField(upload_to='media')
    body = models.TextField()
    
    
    def __str__(self):
        return self.title
