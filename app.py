from flask import Flask, render_template
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """

    import FakeRPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sent')
def sent():
    return render_template('sent.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')