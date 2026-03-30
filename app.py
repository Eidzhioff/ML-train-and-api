from fastapi import FastAPI, Request, HTTPException
import pickle
import pandas as pd
from pydantic import BaseModel
import numpy as np
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import StandardScaler
import json

def prepare_data(data, config):
    X = data

    car_names = X['CarName'].str.split(' ', expand=True).fillna('')
    X['car_company'] = car_names[0]
    X['car_model'] = np.sum(car_names.loc[:, 1:], axis=1)

    X.drop(['CarName'], axis=1, inplace=True)
    
    num_cols = config['num_cols']
    str_cols = config['str_cols']
    bin_cols = config['bin_cols']
    cat_cols = config['cat_cols']

    X['car_company'] = X['car_company'].replace(
        {
            'maxda': 'mazda',
            'porcshce': 'porsche',
            'Nissan': 'nissan',
            'vokswagen': 'volkswagen',
            'vw': 'volkswagen',
            'toyouta': 'toyota',
        }
    )

    enc = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)

    X_train_encoded = enc.fit_transform(X[bin_cols + cat_cols])
    X[bin_cols + cat_cols] = X_train_encoded

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    return X

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

class Input(BaseModel):
    symboling: int
    CarName: object
    fueltype: object
    aspiration: object
    doornumber: object
    carbody: object
    drivewheel: object
    enginelocation: object
    wheelbase: float
    carlength: float
    carwidth: float
    carheight: float
    curbweight: int
    enginetype: object
    cylindernumber: object
    enginesize: int
    fuelsystem: object
    boreratio: float
    stroke: float
    compressionratio: float
    horsepower: int
    peakrpm: int
    citympg: int
    highwaympg: int

app = FastAPI()

@app.get('/status')
def status():
    return {'status': 'ok'}

@app.post('/get_predict')
def get_predict(input_data: Input):
    
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

    create_df = pd.DataFrame({
        'symboling': [input_data.symboling],
        'CarName': [input_data.CarName],
        'fueltype': [input_data.fueltype],
        'aspiration': [input_data.aspiration],
        'doornumber': [input_data.doornumber],
        'carbody': [input_data.carbody],
        'drivewheel': [input_data.drivewheel],
        'enginelocation': [input_data.enginelocation],
        'wheelbase': [input_data.wheelbase],
        'carlength': [input_data.carlength],
        'carwidth': [input_data.carwidth],
        'carheight': [input_data.carheight],
        'curbweight': [input_data.curbweight],
        'enginetype': [input_data.enginetype],
        'cylindernumber': [input_data.cylindernumber],
        'enginesize': [input_data.enginesize],
        'fuelsystem': [input_data.fuelsystem],
        'boreratio': [input_data.boreratio],
        'stroke': [input_data.stroke],
        'compressionratio': [input_data.compressionratio],
        'horsepower': [input_data.horsepower],
        'peakrpm': [input_data.peakrpm],
        'citympg': [input_data.citympg],
        'highwaympg': [input_data.highwaympg],
    })

    data_to_predict = prepare_data(create_df, config=config)
    predict = model.predict(data_to_predict)

    return {'prediction': predict}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)