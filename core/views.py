from django.shortcuts import render
from services.models import Service
from theme.models import SiteSettings


def index(request):
    context = {
        'site_settings': SiteSettings.get_settings(),
        'launch_services': Service.objects.filter(category__slug='launch'),
        'support_services': Service.objects.filter(category__slug='support'),
        'legal_services': Service.objects.filter(category__slug='legal'),
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
