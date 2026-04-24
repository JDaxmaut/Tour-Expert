# -*- coding: utf-8 -*-
from core.models import AdvantageCard, PriceCard

# Clear existing
AdvantageCard.objects.all().delete()
PriceCard.objects.all().delete()

# Advantages
AdvantageCard.objects.create(title="Опыт", description="Более 12 лет в туриндустрии. Знаем все подводные камни и требования регуляторов.", icon_svg='<svg class="w-7 h-7 text-[#1e3a5f]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>', order=1)
AdvantageCard.objects.create(title="Кейсы", description="Успешно запустили десятки туроператоров. Поможем избежать ошибок, которые стоят времени и денег.", icon_svg='<svg class="w-7 h-7 text-[#1e3a5f]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>', order=2)
AdvantageCard.objects.create(title="Надёжность", description="Партнёрство с профильными юристами, налоговыми консультантами, бухгалтерами и маркетологами.", icon_svg='<svg class="w-7 h-7 text-[#1e3a5f]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>', order=3)

# Pricing Cards
desc1 = "- Регистрация ООО\n- Оформление фингарантии\n- Внесение в реестр\n- Пакет договоров\n\nРезультат: полностью легальный бизнес"
PriceCard.objects.create(title="Запуск туроператора под ключ", price_display="от 25 000 ₽", description=desc1, is_highlighted=True, card_type='wide', order=1)
desc2 = "Аудит и настройка процессов: от сайта до взаимодействия с партнёрами. Месяц практической работы."
PriceCard.objects.create(title="Системное сопровождение", price_display="50 000 ₽ / мес", description=desc2, is_highlighted=False, card_type='wide', order=2)

PriceCard.objects.create(title="Пакет договоров", price_display="от 5 000 ₽", description="- С туристами\n- С партнёрами\n- С сотрудниками", card_type='thin', order=3)
PriceCard.objects.create(title="Роскомнадзор", price_display="от 10 000 ₽", description="- Регистрация + аудит сайта (от 10 000 ₽)\n- Пакет документов (от 50 000 ₽)", card_type='thin', order=4)
PriceCard.objects.create(title="Юридические услуги", price_display="от 30 000 ₽", description="- Претензионная работа\n- Судебное сопровождение\n- Защита интересов", card_type='thin', order=5)
PriceCard.objects.create(title="Медиация в туризме", price_display="от 20 000 ₽", description="Досудебное урегулирование конфликтов", card_type='thin', order=6)
PriceCard.objects.create(title="Бухгалтерская консультация", price_display="от 10 000 ₽", description="Налоги, структура, учёт", card_type='thin', order=7)
PriceCard.objects.create(title="Налоговая консультация", price_display="от 10 000 ₽", description="Оптимизация, риски", card_type='thin', order=8)
PriceCard.objects.create(title="Персональная консультация", price_display="от 10 000 ₽", description="Стратегия / разбор кейса", card_type='thin', order=9)
PriceCard.objects.create(title="Регистрация товарного знака", price_display="от 50 000 ₽", description="Полное сопровождение регистрации", card_type='thin', order=10)
