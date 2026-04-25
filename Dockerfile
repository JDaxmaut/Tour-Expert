FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY media ./media
COPY logo.png .
COPY bkg.jpeg .
COPY theme/static_src ./theme/static_src

COPY . .

RUN python manage.py collectstatic --noinput || true

RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='NatalitaMMore').exists() or User.objects.create_superuser('NatalitaMMore', 'admin@tours-expert.ru', '290982nt')" | python manage.py shell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]