from django.db import models

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
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Ценовая карточка"
        verbose_name_plural = "Ценовые карточки"
        ordering = ['order']

    def __str__(self):
        return self.title
