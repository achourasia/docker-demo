FROM python:2-onbuild

RUN apt-get update && apt-get -y install cron

RUN python -c 'import random; import string; print "".join([random.SystemRandom().choice(string.digits + string.letters + string.punctuation) for i in range(100)])' > /etc/django_secretkey.txt && chmod 600 /etc/django_secretkey.txt

RUN python manage.py makemigrations
RUN python manage.py migrate

ADD crontab /etc/cron.d/clean-cron
RUN chmod 0644 /etc/cron.d/clean-cron


CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]
