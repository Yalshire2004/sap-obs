# list of imports
from flask import Flask
from flask import render_template,request,redirect
from transformers import pipeline

# # instanciate flask app
# app = Flask(__name__)

# main route
@app.route("/",methods=["GET"])
def main():
    if request.method == 'GET':
        data={}
        return render_template("index.html",data=data)


# main route
@app.route("/evaluar",methods=["POST"])
def evaluar():
    
    if request.method == 'POST':
        sentiment_pipeline = pipeline("sentiment-analysis")
        data = request.form['texto']
        data=sentiment_pipeline(data)
        return render_template("index.html",data=data)
