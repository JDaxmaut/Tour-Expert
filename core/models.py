from django.db import models


AUDIENCE_PAGES = [
    ('turoperatoram',           'Туроператорам'),
    ('organizatoram-turov',     'Организаторам туров'),
    ('turagentam',              'Турагентам'),
    ('gidam-i-instruktoram',    'Гидам и инструкторам'),
    ('oteliam-i-gostevym-domam','Отелям и гостевым домам'),
]


class AudiencePage(models.Model):
    slug = models.SlugField("URL (slug)", unique=True, allow_unicode=True)
    title = models.CharField("Заголовок", max_length=200)
    subtitle = models.CharField("Подзаголовок", max_length=400, blank=True)
    content = models.TextField("Основной текст", blank=True)
    meta_description = models.CharField("Meta description (SEO)", max_length=300, blank=True)
    is_published = models.BooleanField("Опубликована", default=False)
    order = models.PositiveIntegerField("Порядок в меню", default=0)

    class Meta:
        verbose_name = "Страница аудитории"
        verbose_name_plural = "Страницы аудиторий"
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('audience_page', kwargs={'slug': self.slug})


class AdvantageCard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    icon_svg = models.TextField(verbose_name="SVG иконка (код)")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Карточка преимущества"
        verbose_name_plural = "Карточки преимуществ"
        ordering = ['order']

    def __str__(self):
        return self.title

class FaqItem(models.Model):
    question = models.CharField("Вопрос", max_length=300)
    answer = models.TextField("Ответ (HTML)")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "FAQ — вопрос"
        verbose_name_plural = "FAQ — вопросы"
        ordering = ['order']

    def __str__(self):
        return self.question


class DocumentPage(models.Model):
    DOC_SLUGS = (
        ('offer',   'Договор оферты'),
        ('privacy', 'Политика конфиденциальности'),
        ('consent', 'Согласие на обработку данных'),
        ('terms',   'Пользовательское соглашение'),
    )
    slug = models.CharField("Тип документа", max_length=20, choices=DOC_SLUGS, unique=True)
    title = models.CharField("Заголовок", max_length=200)
    content = models.TextField("Содержимое (HTML)")

    class Meta:
        verbose_name = "Страница документа"
        verbose_name_plural = "Страницы документов"

    def __str__(self):
        return self.title


class CardAccordionItem(models.Model):
    card = models.ForeignKey(
        'PriceCard', on_delete=models.CASCADE, related_name='accordion_items',
        verbose_name="Карточка"
    )
    title = models.CharField("Заголовок пункта", max_length=200)
    content = models.TextField("Содержимое")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Пункт аккордеона"
        verbose_name_plural = "Пункты аккордеона"
        ordering = ['order']

    def __str__(self):
        return f"{self.card.title} — {self.title}"


class InfoPage(models.Model):
    slug = models.SlugField("URL (slug)", unique=True, allow_unicode=True)
    title = models.CharField("Заголовок", max_length=200)
    subtitle = models.CharField("Подзаголовок", max_length=300, blank=True)
    price_display = models.CharField("Цена (текст)", max_length=100, blank=True)
    badge_text = models.CharField("Текст бейджа", max_length=100, blank=True, default='Комплексное решение')
    cta_title = models.CharField("Заголовок CTA", max_length=200, blank=True, default='Готовы начать?')
    cta_text = models.CharField("Текст CTA", max_length=400, blank=True, default='Первая консультация 15 минут — бесплатно. Разберём вашу ситуацию и предложим оптимальное решение.')
    content = models.TextField("Содержимое (HTML)")
    is_published = models.BooleanField("Опубликована", default=False)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Информационная страница"
        verbose_name_plural = "Информационные страницы"
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('info_page', kwargs={'slug': self.slug})


class InfoCard(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    icon_svg = models.TextField(blank=True, null=True, verbose_name="SVG иконка (код)")
    description = models.TextField(blank=True, verbose_name="Краткое описание")
    page = models.ForeignKey(InfoPage, on_delete=models.CASCADE, related_name='cards', verbose_name="Страница")
    audience = models.ForeignKey(
        AudiencePage, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Страница аудитории"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Информационная карточка"
        verbose_name_plural = "Информационные карточки"
        ordering = ['order']

    def __str__(self):
        return self.title


class PriceCard(models.Model):
    CARD_TYPES = (
        ('wide', 'Широкая'),
        ('thin', 'Тонкая'),
    )
    title = models.CharField(max_length=200, verbose_name="Название услуги")
    price_display = models.CharField(max_length=100, verbose_name="Цена (текст)")
    description = models.TextField(blank=True, verbose_name="Описание")
    button_text = models.CharField(max_length=50, default="Заказать", verbose_name="Текст кнопки")
    is_highlighted = models.BooleanField(default=False, verbose_name="Выделенная карточка")
    icon_svg = models.TextField(blank=True, null=True, verbose_name="SVG иконка (код)")
    card_type = models.CharField(max_length=10, choices=CARD_TYPES, default='thin', verbose_name="Тип карточки")
    detail_page = models.ForeignKey(
        InfoPage, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Страница подробнее"
    )
    audience = models.ForeignKey(
        AudiencePage, on_delete=models.SET_NULL, blank=True, null=True,
        verbose_name="Страница аудитории"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Ценовая карточка"
        verbose_name_plural = "Ценовые карточки"
        ordering = ['order']

    def __str__(self):
        return self.title
