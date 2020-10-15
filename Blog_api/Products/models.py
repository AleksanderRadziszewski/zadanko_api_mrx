from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()


class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="CartProducts")


class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.quantity == 0:
            self.delete()
        else:
            super().save(force_insert, force_update, using, update_fields)


# Create your models here.
