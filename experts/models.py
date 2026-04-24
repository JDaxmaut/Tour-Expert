from django.db import models

class Expert(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    photo = models.ImageField(upload_to='experts/', verbose_name="Фото")
    specialization = models.CharField(max_length=200, verbose_name="Специализация")
    bio = models.TextField(verbose_name="О себе / Навыки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Эксперт"
        verbose_name_plural = "Эксперты"
