from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="article/image")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    
    def __str__(self):
        return self.title