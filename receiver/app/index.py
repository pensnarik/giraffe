from flask import render_template, request

from app import app

@app.route('/receive', methods=['POST'])
def receive():
    print('Received data')
    data = request.json
    print(data)
    return 'OK'
