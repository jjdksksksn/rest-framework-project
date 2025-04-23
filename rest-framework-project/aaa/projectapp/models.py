from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.title


class Ads(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title