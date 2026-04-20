from django.contrib import admin
from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'messenger', 'service', 'created_at')
    list_filter = ('service', 'messenger', 'created_at')
    readonly_fields = ('created_at',)
    search_fields = ('name', 'phone', 'email')
