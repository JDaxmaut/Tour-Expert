from django.urls import path
from . import views

urlpatterns = [
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
]
