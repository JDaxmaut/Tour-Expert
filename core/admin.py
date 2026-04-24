from django.contrib import admin
from .models import AdvantageCard, PriceCard

@admin.register(AdvantageCard)
class AdvantageCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(PriceCard)
class PriceCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_display', 'order', 'is_highlighted', 'card_type')
    list_editable = ('order', 'is_highlighted', 'card_type')
