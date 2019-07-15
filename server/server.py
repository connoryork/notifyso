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
    if name in clients:
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
    if name not in clients:
        ## return render_template(404 page)
        return
    # else displays page with button to notify corresponding client
    return  # TODO

@app.route('/notify/{pi_name}')
def notify():
    # check if client is connected
    # if not, redirect to client doesnt exist page
    # send a request to notify the client
    # if request is 404, remove client from client list
    # and redirect to client doesnt exist page?
    pass


def check_client(name):
    return name in clients


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
