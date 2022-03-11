"""Use flask to display temperature convertor, Celsius and Fahrenheit"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def display_home():
    return "<br>Display Celsius in url to covert to Fahrenheit. " \
           "For example <a href ='http://127.0.0.1:5000/f/100'>http://127.0.0.1:5000/f/100</a>" \
           "<br><br>Display Fahrenheit in url to covert to Celsius. " \
           "For example <a href ='http://127.0.0.1:5000/c/100'>http://127.0.0.1:5000/c/100</a>"


@app.route('/<letter>')
def display(letter=""):
    if letter.lower() == "f":
        return "Display Celsius in url to covert to Fahrenheit." \
               "For example: <a href ='http://127.0.0.1:5000/f/100'>http://127.0.0.1:5000/f/100</a>"
    elif letter.lower() == "c":
        return "Display Fahrenheit in url to covert to Celsius." \
               "For example: <a href ='http://127.0.0.1:5000/c/100'>http://127.0.0.1:5000/c/100</a>"


@app.route('/f/<num>')
def f(num=""):
    t_fahrenheit = int(num) * 9.0 / 5 + 32
    return f"{int(num):.2f}°C is {t_fahrenheit:.2f}°F"


@app.route('/c/<num>')
def c(num=""):
    t_celsius = int(num) * 9.0 / 5 + 32
    return f"{int(num):.2f}°F is {t_celsius:.2f}°C"


if __name__ == '__main__':
    app.run()
