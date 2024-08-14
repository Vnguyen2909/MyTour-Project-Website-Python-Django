from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Type_Of_Tour(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    maxGroupSize = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    summary = models.TextField()
    description = models.TextField()
    imageCover = models.ImageField(null=True, blank=True, upload_to="images/")
    type_tour = models.ForeignKey(
        Type_Of_Tour, blank=True, null=True, on_delete=models.SET_NULL
    )
    start_location = models.CharField(max_length=50)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=256, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile/")

    def __str__(self):
        return str(self.user)


class Photo(models.Model):
    tour = models.ForeignKey(Tour, null=True, on_delete=models.SET_NULL)
    images = models.ImageField(null=False, blank=False)


class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, null=True)
    email = models.EmailField(blank=True)
    total_price = models.IntegerField()
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Tour, null=True, on_delete=models.CASCADE)
    price = models.IntegerField()
