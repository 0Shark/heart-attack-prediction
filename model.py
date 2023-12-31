# loading dataset
import pandas as pd
import numpy as np
# visualisation
import matplotlib.pyplot as plt
#EDA
from ydata_profiling import ProfileReport
# data preprocessing
from sklearn.preprocessing import StandardScaler
# data splitting
from sklearn.model_selection import train_test_split
# data modeling
from sklearn.metrics import confusion_matrix,accuracy_score,roc_curve,classification_report
from sklearn.neighbors import KNeighborsClassifier

class Model:
  def __init__(self, data_path):
    self.data = pd.read_csv(data_path)
    self.model = None
    
  def data_preprocessing(self):
    # data profiling
    ProfileReport(self.data)
    # data preprocessing
    y = self.data["target"]
    X = self.data.drop('target',axis=1)
    
    # split the data into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state = 0)

    # feature scaling  
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    return X_train, X_test, y_train, y_test
  
  def model_training(self):
    X_train, X_test, y_train, y_test = self.data_preprocessing()
    # model training
    self.model = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    self.model.fit(X_train, y_train)
    # model evaluation
    y_pred = self.model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    
  def predict(self, data):
    print("Predicting for: ", data)
    # data preprocessing
    data = np.array(data)
    data = data.reshape(1,-1)
    # prediction
    prediction = self.model.predict(data)
    print("Prediction: ", prediction)
    return prediction