import psycopg2
from flask import Flask, g

app = Flask(__name__)

from app import index, db

@app.before_request
def get_db():
    if not hasattr(g, 'conn'):
        g.conn = psycopg2.connect('postgresql://giraffe:giraffe@127.0.0.1:20000')
        g.conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
