from django.contrib import admin
from .models import AdvantageCard, PriceCard, CardAccordionItem, AudiencePage, FaqItem, DocumentPage, InfoCard, InfoPage


@admin.register(AdvantageCard)
class AdvantageCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


class CardAccordionItemInline(admin.TabularInline):
    model = CardAccordionItem
    extra = 1
    fields = ('title', 'content', 'order')


@admin.register(FaqItem)
class FaqItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)


@admin.register(DocumentPage)
class DocumentPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('slug', 'title', 'content')


@admin.register(AudiencePage)
class AudiencePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(InfoPage)
class InfoPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published', 'order')
    list_editable = ('is_published', 'order')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('slug', 'title', 'is_published', 'order')
        }),
        ('Шапка страницы', {
            'fields': ('subtitle', 'badge_text', 'price_display'),
        }),
        ('Контент', {
            'fields': ('content',),
        }),
        ('Блок "Связаться" (CTA)', {
            'fields': ('cta_title', 'cta_text'),
        }),
    )


@admin.register(InfoCard)
class InfoCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'page', 'audience', 'order')
    list_editable = ('order',)
    list_filter = ('audience',)


@admin.register(PriceCard)
class PriceCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_display', 'order', 'is_highlighted', 'card_type', 'detail_page', 'audience')
    list_editable = ('order', 'is_highlighted', 'card_type')
    list_filter = ('audience',)
    inlines = [CardAccordionItemInline]
