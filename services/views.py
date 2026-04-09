from django.shortcuts import get_object_or_404, render
from services.models import Service


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'services/service_detail.html', {'service': service})
