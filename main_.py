from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')

@app.route("/japan")
def hello_japan():
    return "Hello, Japan!!"

@app.route("/japan/<city>")
def hello_japan_city(city):
    return f'Hello, { city } in Japan!!'

@app.route("/america")
def hello_america():
    return "Hello, America!!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)