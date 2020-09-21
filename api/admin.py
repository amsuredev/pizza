from django.contrib import admin
import api.models as models
# Register your models here.
admin.site.register(models.Pizza)
admin.site.register(models.ToppingsInPizza)
admin.site.register(models.Vote)
admin.site.register(models.Topping)
