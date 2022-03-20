FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTOHNUNBUFFERED 1

WORKDIR /code

COPY requirement.txt /code/

RUN pip install pip-upgrade && pip install -r requirement.txt

COPY . /code/

