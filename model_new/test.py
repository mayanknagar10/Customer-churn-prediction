import pickle

f = open("Customer_Churn_Prediction.pkl", 'rb')
model = pickle.load(f)
f.close()


result = model.predict([[640, 46, 3, 0.00, 1, 1, 1, 156260.08, 1, 0, 0, 0, 1]])

print(result)
