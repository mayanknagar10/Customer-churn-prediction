import pickle


data = {
    'credit_score': 619,
    'age': 42,
    'tenure': 2,
    'balance': 0.00,
    'products': 1,
    'credit_card': 1,
    'active_member': 1,
    'salary': 101348.88,
    'location': 'France',
    'gender': 'Female',

}

data['geography_germany'] = 1 if data['location'] == 'Germany' else 0
data['geography_spain'] = 1 if data['location'] == 'Spain' else 0
data['geography_france'] = 1 if data['location'] == 'France' else 0
data['gender_male'] = 1 if data['gender'] == 'Male' else 0
data['gender_female'] = 1 if data['gender'] == 'Feale' else 0


del data['location']
del data['gender']

print(data)
print(list(data.values()))

f = open('Customer_Churn_Prediction.pkl', 'rb')
model = pickle.load(f)
f.close()

result = model.predict([list(data.values())+[0, 0, 0]])
print(result)
