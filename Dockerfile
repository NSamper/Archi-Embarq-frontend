FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log


RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/DjangoProject
COPY dependancies.txt start-server.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY src /opt/app/DjangoProject
WORKDIR /opt/app
RUN pip install -r dependancies.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

WORKDIR /opt/app/DjangoProject
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN python3 manage.py test > test-results.txt

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]