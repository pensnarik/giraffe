FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip3 install psycopg2-binary

ENV LISTEN_PORT 1984
EXPOSE 1984

COPY ./giraffe_api /app/giraffe_api

ENV UWSGI_INI /app/giraffe_api/uwsgi.ini
ENV STATIC_PATH /app/static

RUN echo "postgresql://giraffe:giraffe@giraffe-db/giraffe" > /usr/local/etc/giraffe-api.config
