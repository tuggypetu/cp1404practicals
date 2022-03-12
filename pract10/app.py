from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World! :)</h1>'


@app.route('/greet')
def greet():
    return "<h2> yes Fatty!!</h2>"


@app.route('/greet/<name>')
def greet_yo(name=""):
    return f"Hello {name.title()}, you are A FATTY!!!"


if __name__ == '__main__':
    app.run()
