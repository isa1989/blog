FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt ./requirements.txt

RUN apt-get update && apt-get -y install
RUN pip3 install --upgrade pip
RUN pip3 install -r ./requirements.txt

RUN pip install --upgrade pip pipenv flake8
RUN flake8 --ignore=E501,F401 .


ADD . /code/