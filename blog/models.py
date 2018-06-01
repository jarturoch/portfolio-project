from django.db import models

# Create your models here.

# create blog models
#title
#pub_date
#body
#image
class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField()
    body = models.TextField()
