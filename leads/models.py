from django.db import models
from services.models import Service


class Lead(models.Model):
    name = models.CharField("Имя", max_length=100)
    contact = models.CharField("Контакт (TG/WA/Phone)", max_length=100)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка от {self.name}"
