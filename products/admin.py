from django.contrib import admin
from .models import Brand, Product
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """ Product admin """
    list_display = ('name', 'brand', 'price', 'rating')
    search_fields = ('name', 'brand__name')
    summernote_fields = ('description', 'ingredients')
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(SummernoteModelAdmin):
    """ Brand admin """
    list_display = ('name',)
    search_fields = ('name',)
    summernote_fields = ('description',)
    list_filter = ('created_on',)
    prepopulated_fields = {'slug': ('name',)}
