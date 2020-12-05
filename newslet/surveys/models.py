from django.db import models
from PIL import Image


class Company(models.Model):
    name = models.CharField(max_length=128)
    address_one = models.CharField(max_length=280, default=None)
    address_two = models.CharField(max_length=280, default=None)
    company_logo = models.ImageField(default='logo.jpg', upload_to='company_pics')

    def __str__(self):
        return self.name


    def save(self):
            super().save()

            img = Image.open(self.company_logo.path)

            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.company_logo.path)


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    price = models.FloatField()
    product_logo = models.ImageField(default='product.jpg', upload_to='product_pics')

    def __str__(self):
        return self.name

    def save(self):
            super().save()

            img = Image.open(self.product_logo.path)

            if img.height > 300 or img.width > 300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.imaproduct_logoge.path)


class Survey(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()
    rate_4 = models.IntegerField()
    rate_5 = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product.name
