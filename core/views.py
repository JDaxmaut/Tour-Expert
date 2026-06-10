from django.shortcuts import render, get_object_or_404
from services.models import Service
from theme.models import SiteSettings
from .models import AdvantageCard, PriceCard, AudiencePage, FaqItem, DocumentPage, InfoCard, InfoPage


def index(request):
    context = {
        'site_settings': SiteSettings.get_settings(),
        'launch_services': Service.objects.filter(category__slug='launch'),
        'support_services': Service.objects.filter(category__slug='support'),
        'legal_services': Service.objects.filter(category__slug='legal'),
        'advantages': AdvantageCard.objects.all(),
        'wide_cards': PriceCard.objects.filter(card_type='wide', audience__isnull=True),
        'thin_cards': PriceCard.objects.filter(card_type='thin', audience__isnull=True),
        'info_cards': InfoCard.objects.filter(audience__isnull=True),
        'faq_items': FaqItem.objects.all(),
    }
    return render(request, 'core/index.html', context)


def privacy(request):
    doc = get_object_or_404(DocumentPage, slug='privacy')
    return render(request, 'core/doc.html', {'doc': doc})


def consent(request):
    doc = get_object_or_404(DocumentPage, slug='consent')
    return render(request, 'core/doc.html', {'doc': doc})


def contacts(request):
    return render(request, 'core/contacts.html')


def offer(request):
    doc = get_object_or_404(DocumentPage, slug='offer')
    return render(request, 'core/doc.html', {'doc': doc})


def terms(request):
    doc = get_object_or_404(DocumentPage, slug='terms')
    return render(request, 'core/doc.html', {'doc': doc})


def audience_page(request, slug):
    page = get_object_or_404(AudiencePage, slug=slug, is_published=True)
    context = {
        'page': page,
        'wide_cards': PriceCard.objects.filter(card_type='wide', audience=page),
        'thin_cards': PriceCard.objects.filter(card_type='thin', audience=page),
        'info_cards': InfoCard.objects.filter(audience=page),
    }
    return render(request, 'core/audience.html', context)


def info_page(request, slug):
    page = get_object_or_404(InfoPage, slug=slug, is_published=True)
    return render(request, 'core/info_page.html', {'page': page})


