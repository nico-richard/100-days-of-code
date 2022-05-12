from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/gogole')
def to_google():
    return redirect('http://www.google.com')

if __name__ == '__main__':
    app.run()