from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "this is index"

@app.route('/<name>')
def second(name):
    return "this is %s "% name

if __name__ == '__main__':
    app.run()