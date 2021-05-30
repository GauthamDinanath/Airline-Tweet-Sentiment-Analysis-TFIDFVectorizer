import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    data=request.form['text_field']
    model      =  pickle.load( open('model.pkl','rb'))
    vectorizer =  pickle.load( open('vectorizer.pkl','rb'))
    converted_data= vectorizer.transform([data])
    prediction = model.predict(converted_data)
    #print(prediction)
    #return render_template('index.html', prediction_text='the emotion is $ {}'.format(prediction))
    if prediction[0]==0:
       emotion="positive" 
    if prediction[0]==1:
       emotion="neutral" 
    if prediction[0]==2:
       emotion="negative" 

    return jsonify({"sentiment":emotion})

if __name__ == "__main__":
    app.run(debug=True)