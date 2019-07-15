from flask import Flask, render_template, request, jsonify, escape
import requests

app = Flask(__name__)
clients = {}


####### CLIENT ENDPOINTS #######


@app.route('/connect', methods=['POST'])
def connect():
    content = request.json
    print(content)
    # send test request to pi  TODO

    name = content.get('name')
    address = content.get('address')
    if name is None or address is None:
        return "Name or address is missing, cannot connect", 400
    if client_exists(name):
        return "Name already registered under another client, pick another", 400

    clients[name] = address
    return jsonify(success=True)


####### USER ENDPOINTS #######


@app.route('/')
def index():
    # eventually show list of available client's to notify
    return render_template('index.html')

@app.route('/light/<name>')
def display_notify_page(name):
    # if not, redirect to client doesnt exist page
    name = escape(name)
    if not client_exists(name):
        # return render_template(404 page) TODO
        return
    # else displays page with button to notify corresponding client
    return  # TODO

@app.route('/notify/<name>')
def notify(name):
    name = escape(name)
    if not client_exists(name):
        # return render_template(404 page) TODO
        return

    # send a request to notify the client TODO
    response = requests.post(clients.get(name)) # TODO what message do i want to send here

    if not response.ok:
        clients.pop(name)
        # return render_template(404 page) TODO
        return
    return # TODO stay on same page? return client was successfully notified?


def client_exists(name):
    return name in clients


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
