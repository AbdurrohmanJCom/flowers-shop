from django.contrib.auth.models import User
from django.db import models


class Flower(models.Model):
    title = models.CharField(max_length=75)
    photo = models.CharField(max_length=115, db_index=True)
    is_active = models.BooleanField(default=True)
    rate = models.IntegerField(max_length=1)
    price = models.IntegerField()
    quantity = models.CharField(max_length=25)
    size = models.CharField(max_length=155)
    material = models.CharField(max_length=155)
    additional_info = models.TextField()
    delivery_info = models.TextField()
    description = models.TextField()
    review = models.ForeignKey('shop.Reviews', on_delete=models.CASCADE)


class Reviews(models.Model):
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

