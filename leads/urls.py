from django.urls import path
from leads import views as leads_views

urlpatterns = [
    path('leads/', leads_views.create_lead, name='create_lead'),
]
