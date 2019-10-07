FROM python:slim-stretch AS build

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
EXPOSE 80
CMD ["python3", "herokubot.py"]
