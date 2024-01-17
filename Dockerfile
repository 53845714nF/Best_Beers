FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "Best_Beers.wsgi:application", "--bind", "0.0.0.0:8000"]

EXPOSE 8000
