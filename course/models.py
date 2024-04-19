from django.db import models


class Speciality(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='course/speciality/')
    update_date = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Course(models.Model):
    class PriceType(models.TextChoices):
        s = "USD", "$"
        sum = "UZS", "SO'M"

    title = models.CharField(max_length=40)
    description = models.TextField()
    course_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='course/course/')
    speciality = models.ManyToManyField(Speciality)
    price = models.FloatField()
    price_type = models.CharField(max_length=8, choices=PriceType.choices, default=PriceType.sum)
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