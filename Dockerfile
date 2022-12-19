# syntax=docker/dockerfile:1
FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    binutils \
    libproj-dev \
    libgdal-dev \
    gdal-bin \
    build-essential \
    nano \
    cmake \
    g++

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

RUN python -m pip install -U pip

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code

RUN useradd --no-log-init --uid 9999 --create-home --shell /bin/bash django_user
USER django_user
ENV PATH="/home/django_user/.local/bin:${PATH}"

RUN python -m pip install -r requirements.txt

COPY --chown=django_user:django_user . /code

#RUN python manage.py migrate
RUN python manage.py collectstatic --no-input