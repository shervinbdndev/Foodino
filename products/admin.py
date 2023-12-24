from django.contrib import admin

from .models import Category, Food, Cart, CartItems




class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class FoodModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    


admin.site.register(Category, CategoryModelAdmin)
admin.site.register(Food, FoodModelAdmin)
admin.site.register(Cart)
admin.site.register(CartItems)