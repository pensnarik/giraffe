import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import psycopg2
from flask import render_template, request, jsonify, Response
from werkzeug import FileWrapper
import io

from giraffe_gui import app, db

q_graph = "select v.db_timestamp as dt, v.integer_value, m.name " \
          "from giraffe.metric_value v " \
          "join giraffe.metric m on m.id = v.metric_id " \
          "where v.metric_id = %(metric_id)s " \
          "  and v.db_timestamp >= %(from)s " \
          "  and v.db_timestamp < %(to)s"

@app.route("/graph/<int:metric_id>/<from_dt>/<to_dt>.svg")
def graph(metric_id, from_dt, to_dt):
    #print('from = `%s`, to = `%s`' % (from_dt, to_dt))
    data = db.get_rows(q_graph, {'metric_id': metric_id, 'from': from_dt, 'to': to_dt})
    #print(data)
    dt = np.array([i['dt'] for i in data])
    v = np.array([i['integer_value'] for i in data])
    fig = plt.figure(figsize=(10, 4), dpi=90)
    p_main = fig.add_subplot()
    p_main.plot(dt, v)
    p_main.set(xlabel='time', ylabel=data[0]['name'], title=data[0]['name'])
    p_main.fmt_xdata = mdates.DateFormatter('%Y-%m-%d %H:%M')
    p_main.grid()
    buf = io.BytesIO()
    plt.savefig(buf, format='svg')
    w = FileWrapper(buf)
    buf.seek(0)
    return Response(w, mimetype="image/svg+xml", direct_passthrough=True)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")
