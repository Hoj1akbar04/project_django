from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    street = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.country} {self.city} {self.street}"


class StudentRole(models.TextChoices):
    bakalavr = ("b", "B")
    magistr = ("m", "M")
    ph = ("ph", "PH")


class Students(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/students/')
    birth_date = models.DateField(null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=30, choices=StudentRole.choices, default=StudentRole.bakalavr)

    def __str__(self):
        return f"{self.first_name} {self.last_name} "