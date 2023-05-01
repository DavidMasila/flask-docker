FROM python:3.11.3-bullseye

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip && pip install -r requirements.txt

#we are going to use uwsgi to launch the app 

CMD ["uwsgi","app.ini"]