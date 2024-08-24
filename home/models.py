from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True)
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    picture = models.ImageField(upload_to='media/images')
    body = models.TextField()
    
    class Meta:
        ordering = ["-date_created"]  
    
    def __str__(self):
        return self.title
