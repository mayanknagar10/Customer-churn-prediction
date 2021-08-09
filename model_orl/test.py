import pickle
import numpy as np
import pandas as pd

# file = open('Customer_Churn_Prediction.pkl', 'rb')

# model = pickle.load(file)


def convert():
    pass

# user_data = [619, 'France', 'Female', 42, 2, 0.00, 1, 1, 1, 101348.00]


def robust_scaler(variable):
    var_median = variable.median()
    quartile1 = variable.quantile(0.25)
    quartile3 = variable.quantile(0.75)
    interquantile_range = quartile3 - quartile1
    if int(interquantile_range) == 0:
        quartile1 = variable.quantile(0.05)
        quartile3 = variable.quantile(0.95)
        interquantile_range = quartile3 - quartile1
        if int(interquantile_range) == 0:
            quartile1 = variable.quantile(0.01)
            quartile3 = variable.quantile(0.99)
            interquantile_range = quartile3 - quartile1
            z = (variable - var_median) / interquantile_range
            return round(z, 3)

        z = (variable - var_median) / interquantile_range
        return round(z, 3)
    else:
        z = (variable - var_median) / interquantile_range
    return round(z, 3)


user_data = {
    'credit_score': 619,
    'location': 'France',
    'gender': 'Female',
    'age': 42,
    'tenure': 2,
    'account_balance': 0.00,
    'products': 1,
    'credit_card': 1,
    'active_member': 1,
    'salary': 101348.88
}


user_data['new_tenure'] = user_data['tenure'] / user_data['age']

print(f'newTenure is {user_data["new_tenure"]}')

user_data['credit_score'] = robust_scaler(user_data['credit_score'])

print(user_data)

# print(pd.qcut(619, 6, labels=list(range(1, 7))))


exit()


new_user_data = convert(user_data)

# new_user_dtaa = []

for item in user_data:
    print(item, robust_scaler(item))

result = model.predict(user_data)

print(result)
