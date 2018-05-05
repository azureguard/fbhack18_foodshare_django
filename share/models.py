from django.db import models
from ..users.models import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    amount = models.PositiveIntegerField
    UNIT_CHOICES = (('lt', 'litre'), ('ml', 'millilitre'), ('g', 'grams'))
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)


class Recipe(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)


class RecipeItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    recipe = models.ForeignKey('Recipe', on_delete=models.PROTECT)


class AvailableItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
