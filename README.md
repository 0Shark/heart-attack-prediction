Elmer Dema (22211551)

Juled Zaganjori (22206337)

# Heart Attack Predictor

https://mygit.th-deg.de/ed01551/recomandation-system

## Project Description

Heart Attack Predictor is a desktop application that predicts the probability of a heart attack based on the given data.
The data is taken from Kaggle and the model is trained using the data:
https://www.kaggle.com/datasets/juledz/heart-attack-prediction/

The model is then used to predict the probability of a heart attack as a percentage. 
The prediction is made using a regression model.

## Prerequisites
- Python 3.10.0

## Installation
### Setup the virtual environment

    python -m venv .\venv

### Activate the virtual environment

    .\venv\Scripts\activate

### Install the required packages

    pip install -r .\requirements.txt

## Basic Usage

    python .\gui.py

### Train and test the model

    1) Select the dataset by clicking "Select file" button and choose the dataset file from the dataset folder.
    2) Click "Train" button to train the model.
    3) Click "Predict" button to predict the probability of a heart attack based on the chosen input values.

## Implementation of the Requests

- A Desktop App with PyQT6 has to be developed. [DONE]
- A requirements.txt file must be used to list the used Python modules. [DONE]
- A README.md file must be created with the structure described in part 01. [DONE]
- The module venv must be used. [DONE]
- A free data source must be used. You may find it for example at Kaggle, SciKit (but not the built-in
ones), or other. [DONE]
- There must be a data import (predefined format and content of CSV). [DONE]
- The data must be read from a file after clicking on a (menu) button. [DONE]
- The data must be analyzed with Pandas methods, so that a user gets on overview. [DONE]
- You may use the functions dataframe.info(), dataframe.describe() and/or dataframe.corr()
for that. [DONE]
- You may also use other metrics or diagrams to do this. [DONE]
- Create several input widgets (at least 3, where 2 must be different) that change some feature variables. [DONE]
- A Scikit training model algorithm (e.g. from Aurélien Géron, Chapter 4) must be applied.
- Create 1 or 2 output canvas, i.e. for data visualization [DONE]
- At least 3 statistical metrics over the input data must be shown [DONE]
- The app must react interactively to the change of input parameter with a new prediction with visual-
ization.[DONE]

## Work done

Juled Zaganjori: <br>
- Created the model
- Added GUI input widgets
- Implemented interaction between GUI and model
- Implemented terminal output of the data analysis and prediction

Elmer Dema: <br>
- Created the GUI
- Added GUI input widgets, output canvas and statistical metrics
- Implemented visualization of the data
- Implemented dataset import 
