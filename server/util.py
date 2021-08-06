import json
import pickle
import numpy as np

column_names = None
location = None
model = None


def predict_price(location, total_sqft, bath, balcony, BHK):
    try:
        index = column_names.index(location.lower())
    except:
        index = -1
    x = np.zeros(len(column_names))
    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = BHK
    if index >= 0:
        x[index] = 1
    
    return round(model.predict([x])[0],2)

def get_location():
    return location

def get_artifact():
    print('loading artifact')
    global column_names
    global location
    
    with open('F:/Home_Price_Prediction_Project/server/artifacts/column_names.json', 'r') as f:
        column_names = json.load(f)['data_col']
        location = column_names[4:]
    global model
    with open('./artifacts/model.pickle', 'rb') as f:
        model = pickle.load(f)
    print('done')


#predict_price(location, total_sqft, bath, balcony, BHK)
