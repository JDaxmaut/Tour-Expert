from django.shortcuts import render
from .models import Expert

def expert_list(request):
    experts = Expert.objects.all()
    return render(request, 'experts/list.html', {'experts': experts})
