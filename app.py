from flask import Flask, render_template, request
from random import choice


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        value_dict = {}
        for key, value in request.form.items():
            value_dict[key] = value
        return render_template('index.html', popup=True, msg='The customer will leave the bank' if choice([True, False]) else 'The customer will not leave the bank', hasValues=True, values=value_dict)
    elif request.method == 'GET':
        return render_template('index.html', popup=False, msg='')


if __name__ == '__main__':
    app.run(debug=True)
