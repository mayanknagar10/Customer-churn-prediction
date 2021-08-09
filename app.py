from flask import Flask, render_template, request
from random import choice
import numpy as np
import pickle


app = Flask(__name__)

file = open('./model_new/Customer_Churn_Prediction.pkl', 'rb')
model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        value_dict = {}
        for key, value in request.form.items():
            value_dict[key] = value
        print('\n\n\nValues given by user are')
        print(value_dict)

        valueArray = [float(value_dict['credit_score']), float(
            value_dict['age']), float(value_dict['tenure']), float(value_dict['account_balance']), float(value_dict['products']), float(value_dict['credit_card']), float(value_dict['active_member']), float(value_dict['salary']), 1.0 if value_dict['gender'] == 'female' else 0.0, 1.0 if value_dict['gender'] == 'male'else 0.0, 1.0 if value_dict['location'] == 'France' else 0.0, 1.0 if value_dict['location'] == 'Germany' else 0.0, 1.0 if value_dict['location'] == 'Spain' else 0.0]
        print(valueArray)
        result = model.predict([valueArray])
        print('result is')
        print(result)

        return render_template('index.html', popup=True, msg='The customer will leave the bank' if result[0] else 'The customer will not leave the bank', hasValues=True, values=value_dict)
    elif request.method == 'GET':
        return render_template('index.html', popup=False, msg='')


if __name__ == '__main__':
    app.run(debug=True)
