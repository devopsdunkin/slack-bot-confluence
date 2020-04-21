FROM python:alpine3.11
COPY ./slack-bot-confluence /app

WORKDIR /app

RUN apk --no-cache add gcc=9.2.0-r4 musl-dev=1.1.24-r2 libffi-dev openssl-dev

RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["python", "./app.py"]