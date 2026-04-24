from django.urls import path
from . import views

app_name = 'experts'

urlpatterns = [
    path('', views.expert_list, name='list'),
]
