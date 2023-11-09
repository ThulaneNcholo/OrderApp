from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Categories)
admin.site.register(IngredientsModel)
admin.site.register(MenuItems)
admin.site.register(SpecialsModel)
admin.site.register(RemovedIngredientsModel)
admin.site.register(OrderModel)
admin.site.register(TableOrderModel)
