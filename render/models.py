from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Receipt(models.Model):
    storeName = models.CharField(max_length=200)
    storeAddress = models.CharField(max_length=200)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)  
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.storeName} - {self.totalPrice}"  


class Product(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    nameEnglish = models.CharField(max_length=200)
    nameChinese = models.CharField(max_length=200)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.price}"  
