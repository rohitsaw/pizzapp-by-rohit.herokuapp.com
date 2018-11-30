from django.db import models
import json

# Create your models here.

class Regular_Pizza_Price(models.Model):
    addition = models.CharField(max_length=50)
    small = models.FloatField(max_length=5)
    large = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Regular pizza price'
        verbose_name_plural = 'Regular Pizza Prices'
    
    def __str__(self):
        return f'{self.addition}'
    

class Sicilian_Pizza_Price(models.Model):
    addition = models.CharField(max_length=50)
    small = models.FloatField(max_length=5)
    large = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Sicilian pizza prices'

    def __str__(self):
        return f"{self.addition}"

class toppings(models.Model):
    available_toppings = models.CharField(max_length=65)

    class Meta:
        verbose_name = 'Available Toppings'

    def __str__(self):
        return f"{self.available_toppings}"
    

class Dinner_Platters_Price(models.Model):
    item = models.CharField(max_length=50)
    small = models.FloatField(max_length=5)
    large = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Dinner Platters Price'

    def __str__(self):
        return f"{self.item}"

class Salad_Price(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Salads Price'

    def __str__(self):
        return f"{self.item}"

class Pasta(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Pasta Price'

    def __str__(self):
        return f"{self.item}"


class Sub(models.Model):
    item = models.CharField(max_length=50)
    small = models.CharField(max_length=50, blank =True)
    large = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Sub Price'

    def __str__(self):
        return f"{self.item}"

class Extra(models.Model):
    item = models.CharField(max_length=50)
    price = models.FloatField(max_length=5)

    class Meta:
        verbose_name = 'Extras on Sub'

    def __str__(self):
        return f"{self.item}"


class PlaceOrder(models.Model):
    item = models.TextField()
    price = models.FloatField(max_length=5)
    user = models.CharField(max_length=50)


    # def __str__(self):
    #     return f"{self.user}"








