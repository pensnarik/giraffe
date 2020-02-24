FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip3 install psycopg2-binary numpy matplotlib

COPY ./giraffe_gui /app/giraffe_gui

ENV UWSGI_INI /app/giraffe_gui/uwsgi.ini
ENV STATIC_PATH /app/static

RUN echo "postgresql://web:web@giraffe-db/giraffe" > /usr/local/etc/giraffe-gui.config
