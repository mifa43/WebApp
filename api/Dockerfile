FROM python:3.9.2-slim-buster

ADD ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD ./server.sh ./src /app/

WORKDIR /app

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]
