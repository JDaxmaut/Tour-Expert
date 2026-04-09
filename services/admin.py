from django.contrib import admin
from .models import Category, Service


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'is_flagship', 'result')
    list_filter = ('category', 'is_flagship')
    list_editable = ('price',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'slug', 'category', 'price')
        }),
        ('Детали', {
            'fields': ('is_flagship', 'description', 'result'),
            'classes': ('collapse',)
        }),
    )
