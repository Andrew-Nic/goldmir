from django.db import models

# Create your models here.

class Comment(models.Model):
    Id = models.BigAutoField(primary_key = True)
    User = models.CharField(max_length=50)
    Title = models.CharField(max_length=100)
    Text = models.TextField()
    Date = models.DateTimeField()