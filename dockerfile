FROM python:3

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY main.py ./
COPY parser_1.py ./
COPY database.py ./

RUN pip install beautifulsoup4
RUN pip install requests