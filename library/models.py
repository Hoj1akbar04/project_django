from django.db import models
from student.models import Students


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Comments(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(Students, on_delete=models.CASCADE)
    comment = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} {self.user} {self.comment}"


class Books(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='media/books/')
    count = models.IntegerField(default=1)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comments, blank=True)
    published_date = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.count}"


class Bookings(models.Model):
    user = models.ManyToManyField(Students)
    book = models.ManyToManyField(Books)
    buy_date = models.DateTimeField(auto_now_add=True)
    return_date = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} {self.book} {self.buy_date} {self.return_date}"

