FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/log/app_engine

ADD www/ /usr/share/nginx/www/
RUN chmod -R a+r /usr/share/nginx/www