import importlib, requests
from flask import Flask, render_template

try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO if not available
    """

    import FakeRPi.GPIO as GPIO


app = Flask(__name__)


@app.route('/')
def notify():
    # turn on light
    # if failure, print
    pass

def disconnect():
    # send disconnect request to server
    # exit
    pass

if __name__ == '__main__':
    # confirm a light is plugged in correct port
    # if not, print and exit

    # try connecting to server
    response = requests.post("http://127.0.0.1:5000/connect-pi", json={"path": "something"})
    if response.ok:
        print(response)
    # if cant, retry
    # if never, then print and quit

    #app.run(debug=True, host='0.0.0.0', port=5001)
