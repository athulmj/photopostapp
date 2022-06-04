from django.db import models


class ImageUpload(models.Model):
    author = models.CharField(max_length=50)
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.caption,self.author
