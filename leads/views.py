from django.shortcuts import redirect, render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Lead


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

            # Письмо администратору
            admin_subject = f"Новая заявка от {name}"
            admin_message = f"""
Имя: {name}
Телефон: {phone}
Email: {email}
Удобный способ связи: {messenger_str}

Сообщение:
{message}
            """
            send_mail(
                admin_subject,
                admin_message.strip(),
                settings.DEFAULT_FROM_EMAIL,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,  # Временно для отладки
            )

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
                    fail_silently=True,  # Временно для отладки
                )

            messages.success(request, "Заявка успешно отправлена! Мы свяжемся с вами в ближайшее время.")
            return redirect('index')
    return redirect('index')
