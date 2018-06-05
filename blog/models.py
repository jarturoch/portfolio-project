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

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:150]

    def pub_date_pretty(self):
        return self.date.strftime('%b %e %Y')
