FROM python:3.8-alpine

WORKDIR /app/

COPY requirements.txt requirements.txt

RUN apk add gcc musl-dev libffi-dev openssl-dev python3-dev \
    && python -m pip install --no-cache-dir -r requirements.txt \
    && apk del gcc musl-dev libffi-dev openssl-dev python3-dev 

ADD . /app/

CMD python /app/main.py
