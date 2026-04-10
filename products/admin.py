from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'available', 'created_at') 
    list_display_links = ('name',) 
    list_filter = ('available',) 
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)


