from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy/', views.privacy, name='privacy'),
    path('consent/', views.consent, name='consent'),
]
