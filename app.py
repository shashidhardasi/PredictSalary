import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
finalmodel = pickle.load(open('SalaryPredict.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    exp = float(request.form['Experience'])
    #prediction = finalmodel.predict(np.array(exp))

    

    return render_template('index.html', prediction_text='Expected Salary is  $ {}'.format(exp*10))


if __name__ == "__main__":
    app.run(debug=True)
