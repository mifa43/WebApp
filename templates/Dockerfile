FROM nginx:1.15.8-alpine
#config
copy ./nginx.conf /etc/nginx/nginx.conf
#content , comment out the ones you dont need !
copy ./*.html /usr/share/nginx/html/
copy ./css/*.css /usr/share/nginx/html/
copy ./css/images/*.png /usr/share/nginx/html/
copy ./css/images/*.jpg /usr/share/nginx/html/
copy ./scripts/*.js /usr/share/nginx/html/
