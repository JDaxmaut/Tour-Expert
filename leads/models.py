from django.db import models
from services.models import Service


class Lead(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email", blank=True)
    phone = models.CharField("Телефон", max_length=50, blank=True, default='')
    message = models.TextField("Сообщение", blank=True)
    messenger = models.CharField("Удобный способ связи", max_length=50, blank=True)
    service = models.ForeignKey(
        Service, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"Заявка от {self.name}"
