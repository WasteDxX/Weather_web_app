import flask
import weather
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods =("POST","GET"))
def hello_world():
    return render_template('index.html',temp=weather.temp,weather_img=weather.weather_img)