from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Sale(models.Model):
    url = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)  # in euro
    deliveryPrice = models.DecimalField(max_digits=6, decimal_places=2)  # in euro
    stockQuantity = models.IntegerField()  # approximatif car la boutique n'est pas mise à jour en temps reel
    note = models.IntegerField()  # number of stars
    shop = models.ForeignKey(
        'Shop',
        on_delete=models.CASCADE,
    )
    component = models.ForeignKey(
        'Component',
        on_delete=models.CASCADE,
    )
