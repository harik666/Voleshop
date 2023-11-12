from django.contrib import admin

from ecomapp.models import Category, Product


# Register your models here.


class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CatAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 30
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProdAdmin)
