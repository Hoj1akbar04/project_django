# Generated by Django 5.0.3 on 2024-04-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Slug'),
        ),
    ]
