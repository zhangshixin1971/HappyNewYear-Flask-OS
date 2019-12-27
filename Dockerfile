FROM python:latest

LABEL Author="Shixin Zhang"
LABEL E-mail="zsxabc@hotmail.com"
LABEL version="0.0.1"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "wsgi.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

#RUN pip install --upgrade pip && \
#    pip install pipenv && \
#    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0

