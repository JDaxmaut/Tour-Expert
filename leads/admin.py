from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'service', 'created_at')
    list_filter = ('service', 'created_at')
    readonly_fields = ('created_at',)
