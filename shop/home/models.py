from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255,default='')
    slup = models.CharField(max_length=100,default='')
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product_Featured(models.Model):
    title = models.CharField(max_length=255,default='')
    description = models.TextField(default='')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_img = models.CharField(max_length=255,default='')
    price = models.IntegerField(default=0,null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

