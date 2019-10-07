FROM alpine:3.10
RUN apk --no-cache add python3 tzdata openntpd

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/

RUN apk add --no-cache --virtual .build-deps python3-dev gcc musl-dev openssl-dev libffi-dev && \
 pip3 install --disable-pip-version-check --no-cache-dir -r requirements.txt && \
 apk --purge del .build-deps && \
 rm -f requirements.txt
EXPOSE 80
ENTRYPOINT ["./docker-entrypoint.sh"]
