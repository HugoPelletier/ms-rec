FROM python:3.6.4

RUN pip install --upgrade pip
RUN pip install redis falcon gunicorn

RUN mkdir /code
COPY . /code
WORKDIR /code