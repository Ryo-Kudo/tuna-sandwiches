from flask import Flask
from flask import render_template
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

@app.route("/")
def hello():
    return render_template('index.html')

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