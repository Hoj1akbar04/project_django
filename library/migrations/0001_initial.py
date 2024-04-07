# Generated by Django 5.0.3 on 2024-04-07 14:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateField(auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('count', models.IntegerField(default=1)),
                ('authors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(to='student.students')),
                ('book', models.ManyToManyField(to='library.books')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('published_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.students')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='comments',
            field=models.ManyToManyField(blank=True, to='library.comments'),
        ),
    ]
