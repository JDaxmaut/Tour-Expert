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
        # Поле, которое раньше называлось phone2, теперь может приходить под другим ключом
        # или вообще отсутствовать в POST, судя по логу.
        # В логе я вижу: 'name', 'email', 'phone', 'message', 'messenger', 'consent_offer', 'consent_data'
        # Поля 'phone2', 'telegram', 'whatsapp' в POST нет.
        phone2 = request.POST.get('phone2', '').strip()
        message = request.POST.get('message', '').strip() # В логе поле 'message', а не 'coment'
        service_id = request.POST.get('service_id')

        # Обработка мессенджеров из списка
        messengers = request.POST.getlist('messenger')
        telegram = 'telegram' in messengers
        whatsapp = 'whatsapp' in messengers
        
        # Логируем, что пришло от формы
        print(f"DEBUG: POST data: {request.POST}")
        print(f"DEBUG: Telegram checked: {telegram}, WhatsApp checked: {whatsapp}")

        if name and phone:
            # ... (сохранение в БД) ...

            # Отправка заявки в Яндекс Форму
            survey_id = os.getenv('SURVEY_ID')
            token = os.getenv('YANDEX_FORMS_TOKEN')
            if survey_id and token:
                url = f"https://api.forms.yandex.net/v1/surveys/{survey_id}/form"
                data = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "phone2": phone2 if phone2 else "", # Если поле пустое, передаем пустую строку
                    "coment": message,
                    "telegram": telegram,
                    "whatsapp": whatsapp,
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
                        print(f"Response: {response.read().decode('utf-8')}")
                except urllib.error.HTTPError as e:
                    print(f"Error submitting feedback to Yandex form: {e.code} {e.reason}")
                    error_body = e.read().decode('utf-8')
                    print(f"Response body: {error_body}")
                except Exception as e:
                    print(f"Error submitting feedback to Yandex form: {e}")


            else:
                print("SURVEY_ID or YANDEX_FORMS_TOKEN not set, skipping Yandex form submission")

            messages.success(request, "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")
            return redirect('index')

    return redirect('index')
