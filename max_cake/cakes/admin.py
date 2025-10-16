from django.contrib import admin

from . import models

admin.site.register(models.Cakes)
admin.site.register(models.Categorey)
admin.site.register(models.Shapes) 
admin.site.register(models.Toppings)
admin.site.register(models.Weights)
admin.site.register(models.Flavours)
admin.site.register(models.WishList)