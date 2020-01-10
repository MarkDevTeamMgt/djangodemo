from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField('Name', max_length=100)
    category = models.CharField('Category', max_length=100)
    price = models.IntegerField('Price')

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField('Name', max_length=100)
    address = models.CharField('Address', max_length=1024)
    time = models.DateTimeField('Time', default=timezone.now)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField('Count')

    def __str__(self):
        return '{order} - {product}'.format(order=self.order, product=self.product)
