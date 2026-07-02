# -*- coding: utf-8 -*-
import django, os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from core.models import AudiencePage, PriceCard

turop = AudiencePage.objects.get(slug='turoperatoram')

title = 'Внедрение и подключение к ГИС «Электронная путёвка»'
price = 'от 25 000 ₽'
description = (
    'Настроим подключение к государственной системе, интегрируем '
    'с вашей CRM и обеспечим корректную передачу данных.'
)
icon_svg = '<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>'

# Удаляем существующие карточки (идемпотентность)
PriceCard.objects.filter(title=title, audience__isnull=True).delete()
PriceCard.objects.filter(title=title, audience=turop).delete()

# На главную
PriceCard.objects.create(
    title=title,
    price_display=price,
    description=description,
    button_text='Подробнее',
    is_highlighted=False,
    icon_svg=icon_svg,
    card_type='wide',
    audience=None,
    order=15,
)

# В туроператоры
PriceCard.objects.create(
    title=title,
    price_display=price,
    description=description,
    button_text='Подробнее',
    is_highlighted=False,
    icon_svg=icon_svg,
    card_type='wide',
    audience=turop,
    order=24,
)

print('Готово: карточка «Внедрение и подключение к ГИС «Электронная путёвка»» создана на главной и в туроператорах.')
