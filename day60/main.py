from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def receive_form():
    if request.method == 'POST':
        return request.form
    return request.args


if __name__ == '__main__':
    app.run(debug=True)