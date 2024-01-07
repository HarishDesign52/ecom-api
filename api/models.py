from django.db import models
from .commons import TimeStampModel


# Create your models here.


class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="products/")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.name}'


class Order(TimeStampModel):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"# {self.id}"
