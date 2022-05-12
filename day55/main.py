from flask import Flask, redirect

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return f'<h1><b>{func()}</b></h1>'
    return wrapper

@app.route('/1')
@make_bold
def hello():
    return 'Hello World'

@app.route('/greet-<name>')
def greet(name):
    return f'Nice to meet you {name}'

@app.route('/fu1')
def func_1():
    return 'func_'

@app.route('/fu2/')
def func_2():
    return 'func_2'

if __name__ == '__main__':
    app.run(debug=True)