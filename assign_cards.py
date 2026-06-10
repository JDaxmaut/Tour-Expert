# coding: utf-8
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

import django
django.setup()

from core.models import AudiencePage, PriceCard, CardAccordionItem

pages = {p.slug: p for p in AudiencePage.objects.all()}
cards = {c.id: c for c in PriceCard.objects.all()}

# Assign existing cards to audience pages
assignments = {
    'turoperatoram': [15, 30, 32, 35],
    'organizatoram-turov': [28, 33],
    'turagentam': [31],
    'gidam-i-instruktoram': [29, 36],
}

for slug, ids in assignments.items():
    page = pages[slug]
    for cid in ids:
        c = cards[cid]
        c.audience = page
        c.save()

# New card for oteliam-i-gostevym-domam
hotel_page = pages['oteliam-i-gostevym-domam']
card = PriceCard.objects.create(
    title='Комплект типовых форм договоров по гостевым домам',
    price_display='20 000 \u20bd',
    description='',
    is_highlighted=False,
    card_type='thin',
    audience=hotel_page,
)

items_data = [
    'Договор предоставления услуг гостевого дома (Исполнитель-Заказчик - физические лица)',
    'Договор предоставления услуг гостевого дома (Исполнитель-Заказчик - юридические лица)',
    'Анкета/ Регистрационная карточка гостя',
    'Правила проживания в гостевом доме (Памятка)',
    'Программа производственного контроля за соблюдением санитарно-эпидемиологических требований при оказании услуг гостевого дома',
    'Акт оказания услуг (форма приложения к договору предоставления услуг гостевого дома)',
    'Прейскурант стоимости причиненного ущерба имуществу + Акт оценки ущерба (формы)',
]

for i, title in enumerate(items_data, 1):
    CardAccordionItem.objects.create(
        card=card,
        title=title,
        content='',
        order=i,
    )

print('Done! Cards assigned and new card created.')
