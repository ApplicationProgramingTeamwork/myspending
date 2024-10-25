from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model


class Receipt(models.Model):
    storeName = models.CharField(max_length=200, null=True, blank=True)
    storeAddress = models.CharField(max_length=200, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(null=True,  blank=True, default=timezone.now)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.storeName} - {self.totalPrice}"


class Product(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    nameEnglish = models.CharField(max_length=200, null=True, blank=True)
    nameChinese = models.CharField(max_length=200, null=True, blank=True)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
