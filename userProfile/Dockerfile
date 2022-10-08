FROM python:3.9.2-slim-buster

ENV USERSERVICE_HOST: ${USERSERVICE_HOST_WEBAPP}
ENV USERSERVICE_PORT: ${USERSERVICE_PORT_WEBAPP}
ADD ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD ./server.sh ./src /app/

WORKDIR /app

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]
