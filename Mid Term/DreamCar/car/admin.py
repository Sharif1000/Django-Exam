from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.BrandName)
admin.site.register(models.CarModel)
admin.site.register(models.Buyer)
admin.site.register(models.Comment)