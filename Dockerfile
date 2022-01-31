# syntax=docker/dockerfile:1

FROM python:3.9.2

WORKDIR /flask_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /flask_app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]