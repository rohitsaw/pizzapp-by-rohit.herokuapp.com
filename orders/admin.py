from django.contrib import admin
from .models import Regular_Pizza_Price, Sicilian_Pizza_Price, toppings, PlaceOrder, Dinner_Platters_Price, Salad_Price,Pasta, Sub, Extra
# Register your models here.


admin.site.register(Regular_Pizza_Price)
admin.site.register(Sicilian_Pizza_Price)
admin.site.register(toppings)
admin.site.register(Dinner_Platters_Price),
admin.site.register(Salad_Price)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(Extra)
admin.site.register(PlaceOrder)