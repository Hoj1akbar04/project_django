from django.db import models
from .helpers import SaveMediaFile, Choices

class Speciality(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to=SaveMediaFile.image_speciality)
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    slug = models.SlugField(verbose_name='Slug', max_length=200)
    course_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to=SaveMediaFile.image_course)
    speciality = models.ManyToManyField(Speciality)
    price = models.FloatField()
    status = models.CharField(max_length=15, choices=Choices.CourseStatus.choices, default=Choices.CourseStatus.DRAFT)
    price_type = models.CharField(max_length=8, choices=Choices.PriceType.choices, default=Choices.PriceType.sum)
    active_users = models.PositiveIntegerField(default=0)
    rating = models.FloatField()
    duration_hours = models.IntegerField(default=0)
    duration_minutes = models.IntegerField(default=0)
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.price_type}, {self.active_users}, {self.description}, {self.image}"


class Position(models.Model):
    name = models.CharField(max_length=80)
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    image = models.ImageField(upload_to='course/teacher/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    t_link = models.URLField(null=True, blank=True)
    f_link = models.URLField(null=True, blank=True)
    l_link = models.URLField(null=True, blank=True)
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name}, {self.last_name} {self.email}, {self.position}"