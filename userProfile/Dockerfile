FROM python:3.10-slim-buster

ENV USERSERVICE_HOST: ${USERSERVICE_HOST_WEBAPP}
ENV USERSERVICE_PORT: ${USERSERVICE_PORT_WEBAPP}

ENV CLOUDINARY_CLOUD_NAME: ${CLOUDINARY_CLOUD_NAME}
ENV CLOUDINARY_API_KEY: ${CLOUDINARY_API_KEY}
ENV CLOUDINARY_API_SECRET: ${CLOUDINARY_API_SECRET}

ADD ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

ADD ./server.sh ./src /app/

WORKDIR /app

EXPOSE 8080

CMD ["/bin/bash", "server.sh"]
