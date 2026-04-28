from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('mamunoarab-manebalsuka-8f9d/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('services.urls')),
    path('', include('leads.urls')),
    re_path(r'^.*\.php$', RedirectView.as_view(url='https://i.pinimg.com/236x/3d/03/5c/3d035cf5c1dd05be1964b8b58bee16b3.jpg', permanent=False)),
    re_path(r'^wp(?:\.php)?', RedirectView.as_view(url='https://i.pinimg.com/236x/3d/03/5c/3d035cf5c1dd05be1964b8b58bee16b3.jpg', permanent=False)),
    re_path(r'^wordpress(?:\.php)?', RedirectView.as_view(url='https://i.pinimg.com/236x/3d/03/5c/3d035cf5c1dd05be1964b8b58bee16b3.jpg', permanent=False)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
else:
    from django.views.static import serve
    from django.urls import re_path
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
