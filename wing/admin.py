from django.contrib import admin
from .models import Wing, Course


@admin.register(Wing)
class WingAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['wing', 'title', 'uploaded_by','upload_date',]
  