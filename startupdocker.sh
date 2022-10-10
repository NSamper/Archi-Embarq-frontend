mkdir -p .pip_cache
docker build -t django-project .

docker run -it -p 8020:8020 \
     -e DJANGO_SUPERUSER_USERNAME=admin \
     -e DJANGO_SUPERUSER_PASSWORD=admin \
     -e DJANGO_SUPERUSER_EMAIL=admin@example.com \
     django-project