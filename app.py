from flask import Flask, render_template
import importlib.util
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
def index():
    return render_template('index.html')

@app.route('/sent')
def sent():
    return render_template('sent.html')

@app.route("/readPin/<pin>")
def readPin(pin):
   try:
      GPIO.setup(int(pin), GPIO.IN)
      if GPIO.input(int(pin)) == True:
         response = "Pin number " + pin + " is high!"
      else:
         response = "Pin number " + pin + " is low!"
   except:
      response = "There was an error reading pin " + pin + "."

   templateData = {
      'title' : 'Status of Pin' + pin,
      'response' : response
      }

   return render_template('pin.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
