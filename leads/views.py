from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Lead
import os
import json
import urllib.request


def create_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()
        service_id = request.POST.get('service_id')

        messengers = request.POST.getlist('messenger')
        messenger_str = ', '.join(messengers) if messengers else ''

        if name and phone:
            lead = Lead.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message,
                messenger=messenger_str,
            )
            if service_id:
                from services.models import Service
                try:
                    lead.service = Service.objects.get(id=service_id)
                    lead.save()
                except Service.DoesNotExist:
                    pass

            # Отправка заявки в Яндекс Форму
            survey_id = os.getenv('SURVEY_ID')
            token = os.getenv('YANDEX_FORMS_TOKEN')
            if survey_id and token:
                url = f"https://api.forms.yandex.net/v1/surveys/{survey_id}/form"
                data = {
                    "name": name,
                    "email": email,
                    "telephone": phone,
                    "message": message,
                }
                try:
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(data).encode('utf-8'),
                        headers={
                            'Content-Type': 'application/json',
                            'Authorization': f"OAuth {token}"
                        }
                    )
                    with urllib.request.urlopen(req) as response:
                        print("Feedback submitted to Yandex form")
                except Exception as e:
                    print(f"Error submitting feedback to Yandex form: {e}")
            else:
                print("SURVEY_ID or YANDEX_FORMS_TOKEN not set, skipping Yandex form submission")

            # Письмо клиенту — подтверждение
            if email:
                client_subject = "Заявка принята — ТурЭксперт"
                client_message = f"""
{name}, здравствуйте!

Ваша заявка успешно получена! Мы свяжемся с вами в ближайшее время.

Что было в заявке:
Имя: {name}
Телефон: {phone}
Email: {email}
Сообщение: {message}

Мы ответим вам по удобному способу связи: {messenger_str}

С уважением,
ТурЭксперт
"""
                send_mail(
                    client_subject,
                    client_message.strip(),
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,  # Отключено для отладки
                )

            messages.success(request, "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")
            return redirect('index')

    return redirect('index')
