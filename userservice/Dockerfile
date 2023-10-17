FROM python:3.10-slim-buster

ENV POSTGRES_DB: ${POSTGRES_DB_WEBAPP} # ime baze
ENV POSTGRES_USER: ${POSTGRES_USER_WEBAPP}  # ime korisnika baze
ENV POSTGRES_PASSWORD: ${USER_SERVICE_DB_PASSWORD_WEBAPP}   # sifra baze
ENV POSTGRES_HOST: ${POSTGRES_HOST_WEBAPP}  # ime kontenjera ili localhost

ADD ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD ./server.sh ./src /app/

WORKDIR /app

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]
