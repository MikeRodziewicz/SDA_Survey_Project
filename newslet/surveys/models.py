from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Survey(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()
    rate_4 = models.IntegerField()
    rate_5 = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question
