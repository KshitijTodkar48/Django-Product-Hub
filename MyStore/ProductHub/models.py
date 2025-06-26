from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE = [
        ('EL', 'Electronics'),
        ('CL', 'Clothing and Fashion'),
        ('FD', 'Food and Beverages'),
        ('BT', 'Personal Care and Beauty'),
        ('FT', 'Furniture'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=PRODUCT_TYPE)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name
    

# One to Many relationship. (One product -> Multiple reviews)
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{ self.user.username } review for {self.product.name}'


# Many to Many relationship. (Multiple products -> Multiple sellers)
class Seller(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, related_name='seller')

    def __str__(self):
        return self.name


# One to One relationship. (One product -> One certificate)
class ProductCertificate(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.product.name} issued at {self.issued_date}'