FROM python:slim-stretch AS build

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
COPY . /app/
EXPOSE 80
CMD ["python3", "herokubot.py"]
