import psycopg2
from flask import render_template, request

from app import app, db

q_metric = """select girafee.init_metric(%(name)s, %(description)s)"""
q_metric_value = """insert into giraffe.metric_value(db_timestamp, cluster, db, metric_id, integer_value, numeric_value) """ \
                 """values(%(db_timestamp)s, %(cluster)s, %(db)s, %(metric_id)s, %(integer_value)s, %(numeric_value)s)"""

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    for (cluster_name, metrics) in data.items():
        for metric in metrics:
            db.execute(metric_query, {'db_timestamp': metric['timestamp'], 'cluster': metric['cluster'],
                                      'db': metric['db'], 'metric_id': 1, 'integer_value': metric['value'],
                                      'numeric_value': None})
    return 'OK'

@app.route('/propose', methods=['POST'])
def propose():
    # Receives metric list from receiver
    data = request.json
    for (metric_name, metric) in data.items():
        db.execute(q_metric, {'name': metric_name, 'description': metric['description']})

