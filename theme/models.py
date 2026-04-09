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
        if not SiteSettings.objects.exists():
            super().save(*args, **kwargs)
        else:
            # Update existing instance
            SiteSettings.objects.update(logo=self.logo, hero_image=self.hero_image, about_image=self.about_image)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
