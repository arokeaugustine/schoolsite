# Generated by Django 4.0.6 on 2022-09-16 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wing', '0002_course_title_course_uploaded_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wing',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
