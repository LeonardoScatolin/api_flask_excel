import pandas as pd
from flask_ngrok import run_with_ngrok
from flask import Flask, jsonify
import random as rk

app = Flask(__name__)
run_with_ngrok(app)

d = {
    "name": "Nikola",
    "surname": "Tesla",
    "idade": 60
}

@app.route("/")
def home():
    return "<marquee><h3> OII </h3></marquee>"

@app.route("/input")
def input():
    return jsonify(d)

@app.route("/output", methods=['GET', 'POST'])
def predJson():
    pred = rk.choice(["positive", "negative"])
    nd = d
    nd["prediction"] = pred
    return jsonify(nd)

@app.route("/download_excel")
def download_excel():
    excel_filename = "dados.xlsx"
    try:
        df = pd.read_excel(excel_filename)
        excel_data = df.to_dict(orient="records")  
        dados = jsonify(excel_data)
        return dados  
    except Exception as e:
        return str(e)

app.run()
