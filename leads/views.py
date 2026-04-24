from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Lead
import os
import json
import urllib.request


def create_lead(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        phone2 = request.POST.get('phone2', '').strip()
        message = request.POST.get('coment', '').strip()
        service_id = request.POST.get('service_id')

        # Обработка мессенджеров
        telegram = request.POST.get('telegram', 'off') == 'on'
        whatsapp = request.POST.get('whatsapp', 'off') == 'on'
        
        # Получение чекбоксов (оферта, пд)
        oferta = request.POST.get('oferta', 'off') == 'on'
        pd = request.POST.get('pd', 'off') == 'on'

        messengers = []
        if telegram: messengers.append('Telegram')
        if whatsapp: messengers.append('WhatsApp')
        messenger_str = ', '.join(messengers)

        if name and phone:
            # ... (сохранение в БД остается прежним, предполагаю, что Lead модель адаптирована) ...

            # Отправка заявки в Яндекс Форму
            survey_id = os.getenv('SURVEY_ID')
            token = os.getenv('YANDEX_FORMS_TOKEN')
            if survey_id and token:
                url = f"https://api.forms.yandex.net/v1/surveys/{survey_id}/form"
                data = {
                    "values": {
                        "name": name,
                        "email": email,
                        "phone": phone,
                        "phone2": phone2,
                        "coment": message,
                        "telegram": "Да" if telegram else "Нет",
                        "whatsapp": "Да" if whatsapp else "Нет",
                        "oferta": "Да" if oferta else "Нет",
                        "pd": "Да" if pd else "Нет",
                    }
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
                except urllib.error.HTTPError as e:
                    print(f"Error submitting feedback to Yandex form: {e.code} {e.reason}")
                    print(f"Response body: {e.read().decode('utf-8')}")
                except Exception as e:
                    print(f"Error submitting feedback to Yandex form: {e}")

            else:
                print("SURVEY_ID or YANDEX_FORMS_TOKEN not set, skipping Yandex form submission")

            messages.success(request, "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")
            return redirect('index')

    return redirect('index')
