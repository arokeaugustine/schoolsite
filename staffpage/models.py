from tabnanny import verbose
from django.db import models

# Create your models here.

class Staff(models.Model):
    Rank = models.CharField(max_length=50)
    Name = models.CharField(max_length=150)
    Appointment = models.CharField(max_length=50, blank=True)
    staff_accomplishments = models.CharField(max_length=200, blank=True)
    staff_image = models.ImageField(null=False, blank=False, upload_to="staff_images")

    class Meta:
        ordering = ('Name',)
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self):
        return str(self.Rank+ "  "+self.Name)