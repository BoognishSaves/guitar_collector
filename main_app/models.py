from django.db import models

# Create your models here.
class Guitar(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']




class Artist(models.Model):

    name = models.CharField(max_length=150)
    band = models.CharField(max_length=150)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, related_name="artists")

    def __str__(self):
        return self.name
