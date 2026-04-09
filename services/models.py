from django.db import models


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='services'
    )
    title = models.CharField("Название услуги", max_length=200)
    slug = models.SlugField(unique=True, verbose_name="URL (slug)")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=0)
    is_flagship = models.BooleanField("Флагманский продукт", default=False)
    description = models.TextField("Что внутри (через запятую или списком)")
    result = models.CharField("Ожидаемый результат", max_length=255)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title
