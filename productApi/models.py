from django.db import models


class Signup(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Login(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Plant(models.Model):
    category = models.CharField(max_length=20)
    plant = models.CharField(max_length=20)

    def __str__(self):
        return self.plant


class Order(models.Model):
    name = models.CharField(max_length=20)
    order = models.CharField(max_length=20)

    def __str__(self):
        return self.order







# Add a plant (nursery) (with image, price, name)
# List all plants (user)
# View a plant (user)
# Place order (user)
# View orders (nursery)








