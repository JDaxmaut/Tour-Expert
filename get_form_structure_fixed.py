import os
import json
import urllib.request
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

survey_id = os.getenv('SURVEY_ID')
token = os.getenv('YANDEX_FORMS_TOKEN')

if not survey_id or not token:
    print("Ошибка: SURVEY_ID или YANDEX_FORMS_TOKEN не установлены в .env")
    exit(1)

# УПРОЩЕННЫЙ ЗАПРОС: без /form в конце
url = f"https://api.forms.yandex.net/v1/surveys/{survey_id}"

req = urllib.request.Request(
    url,
    headers={
        'Authorization': f"OAuth {token}"
    }
)

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        # Выводим структуру
        print(json.dumps(data, indent=2, ensure_ascii=False))
except urllib.error.HTTPError as e:
    print(f"Ошибка HTTP: {e.code} {e.reason}")
    print(f"Тело ответа: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Ошибка при получении структуры формы: {e}")
