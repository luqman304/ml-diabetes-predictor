import joblib
import numpy as np

model = joblib.load("diabetes_model.pkl")

def predict_diabetes(data):
    data_array = np.array(data).reshape(1, -1)
    return model.predict(data_array)[0]