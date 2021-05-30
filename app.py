import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    data=request.form['tweet']
    converted_data= vectorizer.transform([data])
    prediction = model.predict(converted_data)
    if prediction[0]==0:
       emotion="positive" 
    if prediction[0]==1:
       emotion="neutral" 
    if prediction[0]==2:
       emotion="negative" 

    return ('the sentiment is	' + emotion)

if __name__ == "__main__":
    model      =  pickle.load( open('model.pkl','rb'))
    vectorizer =  pickle.load( open('vectorizer.pkl','rb'))
    app.run()