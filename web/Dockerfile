#version cua python
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
#app directory
WORKDIR /code


COPY requirements.txt /code/
#cai` thu vien trong file requirements.txt
RUN pip install -r requirements.txt

#copy code
COPY . /code/
CMD gunicorn --bind 0.0.0.0:5001 -w 3 run:app