FROM python:3.7.3

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./src .

CMD uwsgi --module=riesgos.wsgi:application --master --processes 2 --die-on-term --socket webapp:3031