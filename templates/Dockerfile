FROM nginx:1.15.8-alpine
#config

ENV POSTGRES_HOST: ${POSTGRES_HOST_WEBAPP}

COPY ./nginx.conf /etc/nginx/nginx.conf
#content , comment out the ones you dont need !
COPY ./*.html /usr/share/nginx/html/
COPY ./css/*.css /usr/share/nginx/html/
COPY ./css/images/*.png /usr/share/nginx/html/
COPY ./css/images/*.jpg /usr/share/nginx/html/
COPY ./scripts/*.js /usr/share/nginx/html/
