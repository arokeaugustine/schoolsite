from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery_images")
    description = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-upload_date',)
        verbose_name = ('Gallery')
        verbose_name_plural = ('Gallery')

    def __str__(self):
        return self.description

