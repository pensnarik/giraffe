FROM postgres:9.6

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      "python3-pip"

RUN apt-get install -y --no-install-recommends \
    "postgresql-server-dev-9.6" \
    gcc \
    python3-dev \
    libyaml-dev

RUN pip3 install -U pip setuptools psycopg2-binary
RUN pip3 install yandex-pgmigrate

COPY docker/docker-entrypoint-initdb.d /docker-entrypoint-initdb.d/
COPY db /db
RUN sed -i "s/20000/5432/" /db/migrations.yml
WORKDIR /db
