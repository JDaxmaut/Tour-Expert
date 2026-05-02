from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

BOTS_REDIRECT = 'https://youtu.be/xvFZjo5PgG0?si=FpMFFf9rZV_CdPZK'

urlpatterns = [
    path('mamunoarab-manebalsuka-8f9d/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('services.urls')),
    path('', include('leads.urls')),
    # PHP и CMS
    re_path(r'^.*\.php$', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^wp-.*', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^wordpress.*', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^bitrix.*', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^administrator.*', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    # Конфиги и секреты
    re_path(r'^\.env', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^\.git', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^\.vscode', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^\.idea', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^config', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    # Базы и бэкапы
    re_path(r'phpmyadmin', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'pma', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'.*\.sql$', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'.*\.zip$', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'.*\.rar$', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'.*\.tar\.gz$', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'db\.sqlite3', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    # Входы
    re_path(r'^admin/', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^login', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^signin', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^setup', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'^install', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    # Системные пути
    re_path(r'etc/passwd', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'etc/shadow', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
    re_path(r'\.ssh', RedirectView.as_view(url=BOTS_REDIRECT, permanent=False)),
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
