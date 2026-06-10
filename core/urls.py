from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('privacy/', views.privacy, name='privacy'),
    path('consent/', views.consent, name='consent'),
    path('contacts/', views.contacts, name='contacts'),
    path('offer/', views.offer, name='offer'),
    path('terms/', views.terms, name='terms'),
    path('dlya/<slug:slug>/', views.audience_page, name='audience_page'),
    path('info/<slug:slug>/', views.info_page, name='info_page'),
]
