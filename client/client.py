from flask import Flask, render_template

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
    # get port from command line args
    # confirm a light is plugged in correct port
    # if not, print and exit

    # try connecting to server
    # if cant, retry
    # if never, then print and quit

    app.run(debug=True, host='1.1.1.1')