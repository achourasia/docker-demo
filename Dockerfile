FROM python:3.7.3-stretch

ADD . /app
WORKDIR /app

RUN apt-get update -y && apt-get -y install cron

RUN python gen_secret_key.py > /etc/django_secretkey.txt && chmod 600 /etc/django_secretkey.txt

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ADD crontab /etc/cron.d/clean-cron
RUN chmod 0644 /etc/cron.d/clean-cron


CMD [ "bash", "-c", "cron && python ./manage.py runserver 0.0.0.0:8000"]