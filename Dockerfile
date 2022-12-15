FROM python:3.10

RUN apt update -y \
    && apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV HOME=/home/app
ENV APP_HOME=/home/app/web

#ENV STATICFILES_HOME=/tmp/staticfiles

#RUN mkdir -p $STATICFILES_HOME

# WORKDIR is as `cd` + `mkdir`
WORKDIR $APP_HOME

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myproject.asgi:application"]

COPY . .