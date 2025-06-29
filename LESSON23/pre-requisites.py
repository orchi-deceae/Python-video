from flask import Flask, render_template, request
from weather import getCurrWeather

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(host='0.0.0.0', post=8000)