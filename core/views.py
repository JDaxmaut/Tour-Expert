from django.shortcuts import render
from services.models import Service
from theme.models import SiteSettings
from .models import AdvantageCard, PriceCard


def index(request):
    context = {
        'site_settings': SiteSettings.get_settings(),
        'launch_services': Service.objects.filter(category__slug='launch'),
        'support_services': Service.objects.filter(category__slug='support'),
        'legal_services': Service.objects.filter(category__slug='legal'),
        'advantages': AdvantageCard.objects.all(),
        'wide_cards': PriceCard.objects.filter(card_type='wide'),
        'thin_cards': PriceCard.objects.filter(card_type='thin'),
    }
    return render(request, 'core/index.html', context)


def privacy(request):
    return render(request, 'core/privacy.html')


def consent(request):
    return render(request, 'core/consent.html')


def contacts(request):
    return render(request, 'core/contacts.html')


def offer(request):
    return render(request, 'core/offer.html')


def terms(request):
    return render(request, 'core/terms.html')
