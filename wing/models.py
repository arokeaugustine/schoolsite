from distutils.command.upload import upload
from django.db import models
from django.urls import reverse

class Wing(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Wing'
        index_together = (('id', 'slug',),)
        # Verbose_name_plural = 'Wings'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('wing_detail', kwargs={"id": self.id, "slug": self.slug })

class Course(models.Model):
    title = models.CharField(max_length=150, blank=True)
    wing = models.ForeignKey(Wing, on_delete=models.CASCADE)
    course_material = models.FileField(upload_to="course_materials")
    upload_date = models.DateTimeField(auto_now_add=True) 
    uploaded_by = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-upload_date',)
        verbose_name = 'Course'
        # verbose_name_plural = 'Courses'



    



