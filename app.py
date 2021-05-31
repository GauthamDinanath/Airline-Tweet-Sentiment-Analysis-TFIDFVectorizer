import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():

    data=[request.form['tweet']]
    tokenizer.fit_on_texts(data)
    data = tokenizer.texts_to_sequences(data)
    data = pad_sequences(data)
    out=model.predict(data)
    out=np.argmax(out,axis=1)[0]
    if out==0:
       emotion="negative" 
    if out==1:
       emotion="positive" 

    return ('the sentiment is	' + emotion)

if __name__ == "__main__":
    model=tf.keras.models.load_model('model_tf/my_model')
    tokenizer =  pickle.load( open('model_tf/tokenizer.pkl','rb'))
    app.run()