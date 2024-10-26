from django.db import models

class Media(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    sound = models.FileField(upload_to='sounds/')

    def __str__(self):
        return self.title