from django.contrib import admin

# Register your models here.

from .models import Profile, Item, AvailableItem

admin.site.register(Profile)
admin.site.register(Item)
admin.site.register(AvailableItem)