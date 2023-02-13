from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(help_text='Цена в центах')

    def __str__(self):
        return self.name

    def formatter_price(self):
        return self.price / 100


class Discount(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Tax(models.Model):
    name = models.CharField(max_length=255)
    value = models.FloatField(default=0)

    def __str__(self):
        return self.name
class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.FloatField()
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tax = models.ForeignKey(
        Tax,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    def total_price(self):
        self.total_price = sum([item.price for item in self.items.all()])
        if self.discount:
            discounted_price = self.total_price * self.discount.value / 100
        else:
            discounted_price = 0
        if self.tax:
            tax_price = self.total_price * self.tax.value / 100
        else:
            tax_price = 0
        self.total_price = self.total_price - discounted_price - tax_price
        return self.total_price / 100

