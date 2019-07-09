from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)
clients = []


@app.route('/')
def index():
    # eventually show list of available client's to notify
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    # get json body
    content = request.json
    print(content)
    # send test request to pi

    # if good, return good response
    # if bad, return bad response
    return jsonify(success=True)

@app.route('/light/{pi_name}')
def display_notify_page():
    # check if client is connected
    # if not, redirect to client doesnt exist page
    # else displays page with button to notify corresponding client
    pass

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
