from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title