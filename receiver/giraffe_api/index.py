import psycopg2
from flask import render_template, request, jsonify

from giraffe_api import app, db

q_metric       = "select giraffe.init_metric(%(name)s, %(description)s)"
q_metric_value = "insert into giraffe.metric_value" \
                 "(db_timestamp, cluster, db, metric_id, integer_value, numeric_value) " \
                 "values(%(db_timestamp)s, %(cluster)s, %(db)s, %(metric_id)s, " \
                 "%(integer_value)s, %(numeric_value)s)"

@app.route('/receive', methods=['POST'])
def receive():
    data = request.json
    for (cluster_name, metrics) in data.items():
        for metric in metrics:
            db.execute(q_metric_value, {'db_timestamp': metric['timestamp'],
                                        'cluster': metric['cluster'],
                                        'db': metric['db'],
                                        'metric_id': metric['id'],
                                        'integer_value': metric['value'],
                                        'numeric_value': None})
    return 'OK'

@app.route('/propose', methods=['POST'])
def propose():
    # Receives metric list from receiver
    data = request.json
    metrics = {}
    for (metric_name, metric) in data.items():
        id = db.get_value(q_metric, {'name': metric_name, 'description': metric['description']})
        metrics[metric_name] = id
    return jsonify({'result': 'ok', 'metrics': metrics})

@app.route("/", methods=['GET'])
def index():
    return "Everything is OK"
