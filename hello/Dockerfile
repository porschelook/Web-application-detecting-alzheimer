FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN sudo apt update && apt upgrade -y
RUN sudo apt install gettext -y
COPY . /code/
