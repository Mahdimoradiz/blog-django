from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="article/image")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)
    
    class Meta:
        ordering = ["-updated", "created"]
    
    def __str__(self):
        return self.title