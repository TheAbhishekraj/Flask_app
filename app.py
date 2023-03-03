from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/Ajit")
def hello_world1():
    return "Welcome to Hello World, Ajit!"

@app.route("/Nibha")
def hello_world2():
    return "Welcome to Hello World, Nibha!"

@app.route("/Abhishek")
def hello_world3():
    return "Welcome to Hello World, Abhishek!"

@app.route("/Shikha")
def hello_world4():
    return "Welcome to Hello World, Shikha!"

@app.route("/Avinash")
def hello_world5():
    return "Welcome to Hello World, Avinash!"

@app.route("/Neha")
def hello_world6():
    return "Welcome to Hello World, Neha!"

@app.route("/Putru")
def hello_world7():
    return "Welcome to Hello World, Putru!"

@app.route('/test_fun')
def test():
    a = 5+6
    return "this my first fun in flask {}".format(a)

@app.route('/input_url')
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")