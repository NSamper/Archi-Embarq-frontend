FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /opt/app \
    && mkdir -p /opt/app/pip_cache \
    && mkdir -p /opt/app/DjangoProject
COPY dependancies.txt start-server.sh /opt/app/ \
    && .pip_cache /opt/app/pip_cache/ \
    && src /opt/app/DjangoProject
WORKDIR /opt/app
RUN pip install -r dependancies.txt --cache-dir /opt/app/pip_cache \
    && chown -R www-data:www-data /opt/app

WORKDIR /opt/app/DjangoProject
RUN python3 manage.py makemigrations \
    && python3 manage.py migrate \
    && python3 manage.py test > test-results.txt

ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin
ENV DJANGO_SUPERUSER_EMAIL admin@example
ENV APP_SECRET_KEY secret

EXPOSE 8020

STOPSIGNAL SIGTERM

CMD ["/opt/app/start-server.sh"]