# loading dataset
import pandas as pd
import numpy as np
# visualisation
import matplotlib.pyplot as plt
# EDA
from ydata_profiling import ProfileReport
# data preprocessing
from sklearn.preprocessing import StandardScaler
# data splitting
from sklearn.model_selection import train_test_split
# data modeling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

class Model:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = None
        self.scaler = None
    
    def data_preprocessing(self):
        # data profiling
        ProfileReport(self.data)
        # data preprocessing
        y = self.data["target"]
        X = self.data.drop('target', axis=1)
    
        # split the data into train and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

        # feature scaling  
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # store the scaler for later use during prediction
        self.scaler = scaler
    
        return X_train, X_test, y_train, y_test
  
    def model_training(self):
        X_train, X_test, y_train, y_test = self.data_preprocessing()
        # model training with Random Forest Regressor
        self.model = RandomForestRegressor(n_estimators=100, random_state=0)
        self.model.fit(X_train, y_train)
        # model evaluation
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print("Mean Squared Error:", mse)
        print("R-squared:", r2)
    
    def predict(self, data):
        print("Predicting for: ", data)
        # data preprocessing
        data = np.array(data)
        data = data.reshape(1, -1)

        # scale the input data using the stored scaler
        data_scaled = self.scaler.transform(data)

        # prediction
        prediction = self.model.predict(data_scaled)
        print("Prediction: ", prediction)
        return prediction
