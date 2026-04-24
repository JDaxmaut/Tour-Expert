from django.db import models


class SiteSettings(models.Model):
    logo = models.ImageField("Логотип", upload_to='logos/', blank=True, null=True)
    hero_image = models.ImageField("Фото в Hero-секции", upload_to='images/', blank=True, null=True)
    about_image = models.ImageField("Фото в блоке Обо мне", upload_to='images/', blank=True, null=True)

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

    def __str__(self):
        return "Настройки сайта"

    def save(self, *args, **kwargs):
        # Принудительно задаем pk=1, чтобы всегда была одна и та же запись
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
