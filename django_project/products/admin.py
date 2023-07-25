from django.contrib import admin
from .models import Product,Offers


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')


class OffersAdmin(admin.ModelAdmin):
    list_display = ('code','discounts')

admin.site.register(Product,ProductAdmin)
admin.site.register(Offers,OffersAdmin)
