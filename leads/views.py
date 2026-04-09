from django.shortcuts import redirect
from .models import Lead


def create_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        service_id = request.POST.get('service_id')
        if name and contact:
            lead = Lead.objects.create(name=name, contact=contact)
            if service_id:
                from services.models import Service
                try:
                    lead.service = Service.objects.get(id=service_id)
                except Service.DoesNotExist:
                    pass
            lead.save()
            # TODO: здесь можно добавить отправку в Telegram
            return redirect('index')
    return redirect('index')
