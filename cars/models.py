from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    year = models.IntegerField()
    price = models.CharField(max_length=100)

    def str(self):
        return self.brand

class Scooter(models.Model):
    brand = models.CharField(max_length=55)
    model = models.CharField(max_length=55)
    year = models.IntegerField()
    price = models.CharField(max_length=100)

    def str(self):
        return self.brand