from flask import Flask, render_template
import datetime as dt
import requests

app = Flask(__name__)

brands = ['Amazon', 'Apple', 'Microsoft', 'Google', 'Samsung', 'Coca-Cola', 'Toyota', 'Mercedes']
now = dt.datetime.now()

@app.route('/')
def home():
    return render_template('index.html', brands=brands, date=now)
    
@app.route('/name/<string:name>')
def names(name):
    response = requests.get('https://api.genderize.io', params={'name':name}).json()
    return render_template('names.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)