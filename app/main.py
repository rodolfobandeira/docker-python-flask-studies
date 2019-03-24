from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Flask Index Page'

@app.route('/hello/<name>')
def hello(name):
    return 'Hello World %s' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

