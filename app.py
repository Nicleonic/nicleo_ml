import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
model = pickle.load(open('model/mymodel.pkl', 'rb'))

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('prediction.html', pageTitle="prediction")

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['surface'])
    
    prediction = model.predict([[area]])

    output = round(prediction[0][0], 2)

    return render_template('prediction.html', pred='Prix de {} pieds carré est {} Euro(s)'.format(area, output))

if __name__ == '__main__':
    app.run(port=4400, debug=True)