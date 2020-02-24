import psycopg2
from flask import Flask, g

app = Flask(__name__)

from giraffe_api import index, db

@app.before_request
def get_db():
    if not hasattr(g, 'conn'):
        with open('/usr/local/etc/giraffe-api.config', 'rt') as f:
            dsn = f.read().strip()

        g.conn = psycopg2.connect(dsn)
        g.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
