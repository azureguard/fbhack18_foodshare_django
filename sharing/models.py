from django.db import models


class ItemManager(models.Manager):
    def create_user(self, name, university, address, email, password):
        user = self.create(name=name, university=university, address=address,
                           email=email, password=password)
        return user

    def create_recipe(self):
        pass

    def create_share(self):
        pass


class Item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    amount = models.PositiveIntegerField
    UNIT_CHOICES = (('lt', 'litre'), ('ml', 'millilitre'), ('g', 'grams'))
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)


class Recipe(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    items = models.ManyToManyField('Item')


class AvailableItem(models.Model):
    item = models.ForeignKey('Item', on_delete=models.PROTECT)
    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
