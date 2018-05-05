from django.db import models
from django.contrib.auth.models import User


class ItemManager(models.Manager):
    def create_item(self, name, category, amount, unit):
        item = self.create(name=name, type=category, amount=amount, unit=unit)
        return item


class RecipeManager(models.Manager):
    def create_recipe(self, name):
        recipe = self.create(user=User.first_name, name=name, items=Item.name)
        return recipe


class AvailableItemManager(models.Manager):
    def create_availableitem(self):
        availableitem = self.create()
        return availableitem


class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    amount = models.PositiveIntegerField
    UNIT_CHOICES = (('lt', 'litre'), ('ml', 'millilitre'), ('g', 'grams'))
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)


class Recipe(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    items = models.ManyToManyField('Item')


class AvailableItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)