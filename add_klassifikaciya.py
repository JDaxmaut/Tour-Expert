# -*- coding: utf-8 -*-
from core.models import AudiencePage, PriceCard, InfoPage

hotels = AudiencePage.objects.get(slug='oteliam-i-gostevym-domam')

# Idempotent: удалить если уже есть
InfoPage.objects.filter(slug='klassifikaciya-gostinits').delete()
PriceCard.objects.filter(
    title='Классификация гостиниц, хостелов и мини-отелей',
    audience=hotels
).delete()

# ── HTML-контент для страницы «Подробнее» ────────────────────────────────────

content = """
<div>
<h2>О классификации</h2>
<p>Классификация средств размещения — обязательная процедура для гостиниц, хостелов и мини-отелей в соответствии с действующим законодательством РФ. Наличие официально присвоенной категории необходимо для законной деятельности и приёма гостей.</p>
<p>Мы проводим экспертную оценку объекта, помогаем с подготовкой документов и сопровождаем на каждом этапе — от самооценки до получения свидетельства и внесения в федеральный реестр классифицированных средств размещения.</p>
</div>

<div>
<h2>Что входит в классификацию</h2>
<ul>
<li>Анализ объекта и предварительная оценка соответствия критериям звёздной категории</li>
<li>Подготовка и проверка комплекта документов для самооценки</li>
<li>Подача заявки в аккредитованную классификационную организацию</li>
<li>Сопровождение выездной экспертной проверки</li>
<li>Контроль получения свидетельства о присвоении категории</li>
<li>Содействие во внесении сведений в федеральный реестр классифицированных средств размещения</li>
</ul>
</div>

<div>
<h2>Стоимость классификации</h2>
<p>В рублях. НДС не облагается — применяется упрощённая система налогообложения.</p>
<div class="table-scroll">
<table>
<thead>
<tr>
<th>Категория</th>
<th>До 15</th>
<th>16–25 *<br>26–50 **</th>
<th>51–100</th>
<th>101–150</th>
<th>151–200</th>
<th>201–250</th>
<th>251–300</th>
<th>301–350 *<br>351–400 **</th>
<th>401–600 *<br>601–800 **</th>
<th>Свыше 800</th>
</tr>
</thead>
<tbody>
<tr>
<td>1 звезда</td>
<td>19 200</td>
<td>24 400</td>
<td>30 700</td>
<td>33 800</td>
<td>36 900</td>
<td>42 100</td>
<td>47 300</td>
<td><div class="dual"><span class="d1">49 400 *</span><span class="d2">51 500 **</span></div></td>
<td><div class="dual"><span class="d1">56 700 *</span><span class="d2">66 600 **</span></div></td>
<td>71 800</td>
</tr>
<tr>
<td>2 звезды</td>
<td>21 300</td>
<td>26 500</td>
<td>34 300</td>
<td>39 000</td>
<td>44 200</td>
<td>48 400</td>
<td>54 100</td>
<td><div class="dual"><span class="d1">55 600 *</span><span class="d2">57 700 **</span></div></td>
<td><div class="dual"><span class="d1">61 900 *</span><span class="d2">68 100 **</span></div></td>
<td>74 400</td>
</tr>
<tr>
<td>3 звезды</td>
<td>26 500</td>
<td><div class="dual"><span class="d1">31 500 *</span><span class="d2">36 900 **</span></div></td>
<td>49 500</td>
<td>57 700</td>
<td>62 400</td>
<td>67 600</td>
<td>73 100</td>
<td><div class="dual"><span class="d1">77 000 *</span><span class="d2">82 200 **</span></div></td>
<td><div class="dual"><span class="d1">93 000 *</span><span class="d2">103 700 **</span></div></td>
<td>110 200</td>
</tr>
<tr>
<td>4 звезды</td>
<td>43 700</td>
<td><div class="dual"><span class="d1">48 700 *</span><span class="d2">53 700 **</span></div></td>
<td>71 800</td>
<td>77 000</td>
<td>83 700</td>
<td>87 900</td>
<td>93 100</td>
<td><div class="dual"><span class="d1">96 700 *</span><span class="d2">100 400 **</span></div></td>
<td><div class="dual"><span class="d1">119 300 *</span><span class="d2">135 200 **</span></div></td>
<td>142 000</td>
</tr>
<tr>
<td>5 звёзд</td>
<td>57 500</td>
<td>74 900</td>
<td>89 400</td>
<td>96 700</td>
<td>104 000</td>
<td>110 800</td>
<td>119 600</td>
<td><div class="dual"><span class="d1">122 700 *</span><span class="d2">126 900 **</span></div></td>
<td><div class="dual"><span class="d1">135 200 *</span><span class="d2">166 400 **</span></div></td>
<td>172 100</td>
</tr>
</tbody>
</table>
</div>
<p class="table-note">* — номерной фонд 16–25 / 301–350 / 401–600 номеров &nbsp;&nbsp;|&nbsp;&nbsp; ** — номерной фонд 26–50 / 351–400 / 601–800 номеров</p>
</div>

<div>
<h2>Дополнительные услуги</h2>
<ul>
<li>Предварительная оценка объекта с выездом эксперта — <strong>от 10 000 ₽</strong></li>
<li>Консультации по вопросам классификации — <strong>от 5 000 ₽</strong></li>
<li>Помощь в прохождении самооценки — <strong>от 11 000 ₽</strong></li>
</ul>
</div>

<div>
<h2>Юридические услуги для средств размещения</h2>
<ul>
<li>Содействие в получении статуса туроператора по въездному туризму для оформления приглашений иностранным гражданам</li>
<li>Подготовка документов для внесения изменений в ЕГРЮЛ, комплексное сопровождение процедуры (в том числе для компаний из регионов)</li>
<li>Юридическая экспертиза, разработка и актуализация договоров с партнёрами и поставщиками услуг</li>
<li>Оперативная правовая поддержка при претензиях со стороны гостей: анализ рисков, судебная перспектива, минимизация финансовых и репутационных потерь</li>
</ul>
</div>

<div>
<h2>Медиация</h2>
<p>Альтернативный способ урегулирования конфликтов. Помогаем решать споры с гостями без суда — быстро, конфиденциально и с минимальными репутационными рисками для вашего объекта.</p>
</div>
"""

info_page = InfoPage.objects.create(
    slug='klassifikaciya-gostinits',
    title='Классификация гостиниц, хостелов и мини-отелей',
    subtitle='Полное сопровождение на всех этапах получения категории от 1 до 5 звёзд',
    price_display='от 19 200 ₽',
    badge_text='Средства размещения',
    cta_title='Нужна классификация?',
    cta_text='Оставьте заявку — разберём ваш объект и рассчитаем стоимость в течение 1 рабочего дня.',
    content=content,
    is_published=True,
    order=10,
)

icon_svg = '<svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>'

card_description = (
    'Помогаем пройти классификацию средств размещения в соответствии с действующими '
    'требованиями законодательства. Сопровождаем гостиницы, хостелы и мини-отели '
    'на всех этапах получения категории 1–5 звёзд: от подготовки документов и '
    'самооценки до выездной проверки и внесения в федеральный реестр.'
)

PriceCard.objects.create(
    title='Классификация гостиниц, хостелов и мини-отелей',
    price_display='от 19 200 ₽',
    description=card_description,
    button_text='Подробнее',
    is_highlighted=False,
    icon_svg=icon_svg,
    card_type='wide',
    detail_page=info_page,
    audience=hotels,
    order=5,
)

print('Готово: InfoPage и PriceCard успешно созданы.')
print(f'  InfoPage slug: {info_page.slug}')
print(f'  URL: /info/{info_page.slug}/')
