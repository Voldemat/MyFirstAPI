FROM python:3.9

ENV PYTHONDONTWRITEBITECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN pip install pipenv

RUN pipenv install --system --deploy --dev

RUN cp wheels/django-rest-swagger/index.html /usr/local/lib/python3.9/site-packages/rest_framework_swagger/templates/rest_framework_swagger
