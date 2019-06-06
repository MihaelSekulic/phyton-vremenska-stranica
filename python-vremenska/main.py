# glavni program

import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    grad = "Zagreb"

    unit = "metric"

    apikey = "4164d2c18d5dbe175fc32c8f4be7bfbf"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())

@app.route("/split", methods=["GET"])
def split():

    grad = "Split"

    unit = "metric"

    apikey = "4164d2c18d5dbe175fc32c8f4be7bfbf"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("split.html", data=data.json())

@app.route("/rijeka", methods=["GET"])
def rijeka():

    grad = "Rijeka"

    unit = "metric"

    apikey = "4164d2c18d5dbe175fc32c8f4be7bfbf"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("rijeka.html", data=data.json())

@app.route("/osijek", methods=["GET"])
def osijek():

    grad = "Osijek"

    unit = "metric"

    apikey = "4164d2c18d5dbe175fc32c8f4be7bfbf"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=hr".format(grad, unit, apikey)

    data = requests.get(url=url)

    return render_template("osijek.html", data=data.json())


if __name__ =="__main__":
    app.run()