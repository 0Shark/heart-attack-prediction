# dataset: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset/
# https://www.kaggle.com/code/nareshbhat/heart-attack-prediction-using-different-ml-models/notebook

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QGridLayout, QSlider, QHBoxLayout, QSpinBox, QDial, QProgressBar, QDialog, QFileDialog, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heart Attack Risk Calculator")
        self.resize(750, 550)
        self.tabs_section()        
        self.tabs.setCurrentIndex(0)
        self.setWindowIcon(QIcon("heart.png"))
        self.display_home()


    def tabs_section(self):
        self.tabs = QTabWidget(self)
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setMovable(True)

        # Show all tabs without arrow buttons
        self.tabs.setDocumentMode(True)

        tab1 = QWidget()
        tab2 = QWidget()

        self.tabs.addTab(tab1, "Home")
        self.tabs.addTab(tab2, "Visualization")

        # Set elide mode for tab text (adjust as needed)
        self.tabs.setElideMode(Qt.TextElideMode.ElideRight)

        self.tabs.currentChanged.connect(self.tab_changed)

        # Create a layout for the main widget
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tabs)

        # Set the layout for the main widget
        self.setLayout(main_layout)

    def tab_changed(self, index):
        if index == 0:
            self.display_home()
        elif index == 1:
            self.display_visualization()

    def display_home(self):
        # Create a widget for the home tab
        home_tab_widget = QWidget()
        grid_layout = QGridLayout(home_tab_widget)

        # Gender
        self.gender_label = QLabel("Gender: ")
        self.gender_group = QButtonGroup()
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        # Set the default checked button
        self.male_radio.setChecked(True)
        self.gender_group.buttonClicked.connect(self.value_changed)

        # Age label and slider
        self.slider_age = QSlider(Qt.Orientation.Horizontal)
        self.slider_age.setMaximumWidth(120)
        self.slider_age.setMinimum(29)
        self.slider_age.setMaximum(77)
        self.slider_age.setValue(53)
        self.slider_age.setTickInterval(1)
        self.slider_age.valueChanged.connect(self.value_changed)
        self.label_slider_age = QLabel("Age: " + str(self.slider_age.value()))

        # Chest Pain Type
        self.chest_pain_type=QSpinBox()
        self.chest_pain_type.setMinimumWidth(100)
        self.chest_pain_type.setMaximumWidth(120)
        self.chest_pain_type.setMinimum(0)
        self.chest_pain_type.setMaximum(3)
        self.chest_pain_type.setValue(0)
        self.chest_pain_type.setSingleStep(1)
        self.slider_age.valueChanged.connect(self.value_changed)
        self.chest_pain_type_label = QLabel("Chest Pain Type: " + str(self.chest_pain_type.value()))
        self.chest_pain_type.valueChanged.connect(self.value_changed)

        # Cholestoral Dial
        self.cholestoral_dial= QDial()
        self.cholestoral_dial.setMinimum(126)
        self.cholestoral_dial.setMaximum(564)
        self.cholestoral_dial.setValue(250)
        self.cholestoral_dial.setNotchesVisible(True)
        self.cholestoral_dial.valueChanged.connect(self.value_changed)
        self.cholestoral_dial_label = QLabel("Cholestoral: " + str(self.cholestoral_dial.value()))
        self.cholestoral_dial_label.setAlignment(Qt.AlignmentFlag.AlignLeft) 
        
        # Maximum heart rate achieved
        self.maximum_heart_rate_achieved=QDial()
        self.maximum_heart_rate_achieved.setMinimum(71)
        self.maximum_heart_rate_achieved.setMaximum(202)
        self.maximum_heart_rate_achieved.setValue(150)
        self.maximum_heart_rate_achieved.setNotchesVisible(True)
        self.maximum_heart_rate_achieved.valueChanged.connect(self.value_changed)
        self.maximum_heart_rate_achieved_label = QLabel("Maximum Heart Rate Achieved: " + str(self.maximum_heart_rate_achieved.value()))
        self.maximum_heart_rate_achieved_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        #resting blood pressure
        self.resting_blood_pressure=QDial()
        self.resting_blood_pressure.setMinimum(94)
        self.resting_blood_pressure.setMaximum(200)
        self.resting_blood_pressure.setValue(130)
        self.resting_blood_pressure.setNotchesVisible(True)
        self.resting_blood_pressure.valueChanged.connect(self.value_changed)
        self.resting_blood_pressure_label = QLabel("Resting Blood Pressure: " + str(self.resting_blood_pressure.value()))
        self.resting_blood_pressure_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        
        # Resting electrocardiographic results (values 0,1,2)
        self.resting_electrocardiographic_results = QSpinBox()
        self.resting_electrocardiographic_results.setMinimumWidth(120)
        self.resting_electrocardiographic_results.setMaximumWidth(120)
        self.resting_electrocardiographic_results.setMinimum(0)
        self.resting_electrocardiographic_results.setMaximum(2)
        self.resting_electrocardiographic_results.setValue(0)
        self.resting_electrocardiographic_results.setSingleStep(1)
        self.slider_age.valueChanged.connect(self.value_changed)
        self.resting_electrocardiographic_results_label = QLabel("Resting Electrocardiographic Results: " + str(self.resting_electrocardiographic_results.value()))
        self.resting_electrocardiographic_results.valueChanged.connect(self.value_changed)
        
        # fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
        self.fasting_blood_sugar = QCheckBox("Fasting Blood Sugar > 120 mg/dl")
        self.fasting_blood_sugar.setChecked(False)
        self.fasting_blood_sugar.stateChanged.connect(self.value_changed)
        
        # exercise induced angina (1 = yes; 0 = no)
        self.exercise_induced_angina = QCheckBox("Exercise Induced Angina")
        self.exercise_induced_angina.setChecked(False)
        self.exercise_induced_angina.stateChanged.connect(self.value_changed)
        
        # st depression induced by exercise relative to rest
        self.st_depression_induced_by_exercise_relative_to_rest = QSpinBox()
        self.st_depression_induced_by_exercise_relative_to_rest.setMinimumWidth(120)
        self.st_depression_induced_by_exercise_relative_to_rest.setMaximumWidth(120)
        self.st_depression_induced_by_exercise_relative_to_rest.setMinimum(0)
        self.st_depression_induced_by_exercise_relative_to_rest.setMaximum(6)
        self.st_depression_induced_by_exercise_relative_to_rest.setValue(0)
        self.st_depression_induced_by_exercise_relative_to_rest.setSingleStep(1)
        self.st_depression_induced_by_exercise_relative_to_rest.valueChanged.connect(self.value_changed)
        self.st_depression_induced_by_exercise_relative_to_rest_label = QLabel("ST Depression Induced By Exercise Relative To Rest: " + str(self.st_depression_induced_by_exercise_relative_to_rest.value()))
        
        # select label
        self.btn_open_dialog = QPushButton('Select File', self)
        self.btn_open_dialog.setMaximumWidth(90)
        self.btn_open_dialog.clicked.connect(self.show_file_dialog)

        self.textbox_file_path = QLineEdit(self)
        self.textbox_file_path.setMaximumWidth(200)
        self.textbox_file_path.setReadOnly(True)
        self.textbox_file_path.setText("No file selected")

        # Result label
        result_label = QLabel("Result:")
        

        # Calculate heart attack risk
        go_button = QPushButton("Train")
        go_button.setMaximumWidth(80)
        go_button.clicked.connect(self.train)
        
        # Gender
        grid_layout.addWidget(self.gender_label, 0, 0)
        grid_layout.addWidget(self.gender_label, 0, 0)
        grid_layout.addWidget(self.male_radio, 1, 0)
        grid_layout.addWidget(self.female_radio, 1, 1)

        # Age slider
        grid_layout.addWidget(self.label_slider_age, 2, 0)
        grid_layout.addWidget(self.slider_age, 3, 0, 1, 2)

        # Resting blood pressure
        grid_layout.addWidget(self.resting_blood_pressure_label, 4, 0)
        grid_layout.addWidget(self.resting_blood_pressure, 5, 0)
        
        # Resting electrocardiographic results
        grid_layout.addWidget(self.resting_electrocardiographic_results_label, 2, 2)
        grid_layout.addWidget(self.resting_electrocardiographic_results, 3, 2)

        # Chest pain type
        grid_layout.addWidget(self.chest_pain_type_label, 6, 0)
        grid_layout.addWidget(self.chest_pain_type, 7, 0)
        
        # Fasting blood sugar
        grid_layout.addWidget(self.fasting_blood_sugar, 9, 0)
        
        # Exercise induced angina
        grid_layout.addWidget(self.exercise_induced_angina, 10, 0)
        
        # ST depression induced by exercise relative to rest
        grid_layout.addWidget(self.st_depression_induced_by_exercise_relative_to_rest_label, 4, 2)
        grid_layout.addWidget(self.st_depression_induced_by_exercise_relative_to_rest, 5, 2)

        # Cholestoral dial
        grid_layout.addWidget(self.cholestoral_dial_label, 0, 2)
        grid_layout.addWidget(self.cholestoral_dial, 1, 2)
        
        # Maximum heart rate achieved
        grid_layout.addWidget(self.maximum_heart_rate_achieved_label, 6, 2)
        grid_layout.addWidget(self.maximum_heart_rate_achieved, 7, 2)

        #result label
        grid_layout.addWidget(result_label, 8, 2)
        #file path
        grid_layout.addWidget(self.btn_open_dialog, 9, 2)
        grid_layout.addWidget(self.textbox_file_path, 9, 1)
        #go label
        grid_layout.addWidget(go_button, 10, 2)

        home_tab_widget.setLayout(grid_layout)
        # Check if a layout already exists for the home tab
        if self.tabs.widget(0).layout():
            # Clear the existing layout for the home tab
            for i in reversed(range(self.tabs.widget(0).layout().count())):
                self.tabs.widget(0).layout().itemAt(i).widget().setParent(None)

        # Set the layout for the current tab
        self.tabs.widget(0).setLayout(QVBoxLayout(self.tabs.widget(0)))
        self.tabs.widget(0).layout().addWidget(home_tab_widget)


    def display_visualization(self):
        pass

    def value_changed(self):
        self.label_slider_age.setText("Age: " + str(self.slider_age.value()))
        self.chest_pain_type_label.setText("Chest Pain Type: " + str(self.chest_pain_type.value()))
        self.cholestoral_dial_label.setText("Cholestoral: " + str(self.cholestoral_dial.value()))
        self.resting_blood_pressure_label.setText("Resting Blood Pressure: " + str(self.resting_blood_pressure.value()))
        self.resting_electrocardiographic_results_label.setText("Resting Electrocardiographic Results: " + str(self.resting_electrocardiographic_results.value()))
        self.st_depression_induced_by_exercise_relative_to_rest_label.setText("ST Depression Induced By Exercise Relative To Rest: " + str(self.st_depression_induced_by_exercise_relative_to_rest.value()))
        self.maximum_heart_rate_achieved_label.setText("Maximum Heart Rate Achieved: " + str(self.maximum_heart_rate_achieved.value()))
        # print changes in the terminal and flush the output
        # Clear the terminal
        print("\033c", end="")
        print("------------------ SETUP VALUES -----------------")
        print(f"Gender: {self.gender_group.checkedButton().text()}")
        print(f"Age: {self.slider_age.value()}")
        print(f"Chest Pain Type: {self.chest_pain_type.value()}")
        print(f"Cholestoral: {self.cholestoral_dial.value()}")
        print(f"Resting Blood Pressure: {self.resting_blood_pressure.value()}")
        print(f"Fasting Blood Sugar > 120 mg/dl: {self.fasting_blood_sugar.isChecked()}")
        print(f"Resting Electrocardiographic Results: {self.resting_electrocardiographic_results.value()}")
        print(f"Exercise Induced Angina: {self.exercise_induced_angina.isChecked()}")
        print(f"ST Depression Induced By Exercise Relative To Rest: {self.st_depression_induced_by_exercise_relative_to_rest.value()}")
        print(f"Maximum Heart Rate Achieved: {self.maximum_heart_rate_achieved.value()}")
        print("-------------------------------------------------")
        
        
        
    
    def train(self):
        if self.check_dataset():
            progress_dialog = ProgressDialog(self)
            progress_dialog.exec()
    
    def show_file_dialog(self):
        file_dialog = QFileDialog(self)
        # checks if the user selected a file and pastes the path in the textbox
        """ check if the user selected file is a csv file(unfinished!)"""
        if file_dialog.exec():
            self.textbox_file_path.setText(file_dialog.selectedFiles()[0])
        

    def update_progress(self, progress_bar, timer):
        current_value = progress_bar.value()
        new_value = (current_value + 1) % (progress_bar.maximum() + 1)
        progress_bar.setValue(new_value)

        if new_value == 0:
            timer.stop()


    def check_dataset(self):
        try:
            file=pd.read_csv(self.textbox_file_path.text())
            file.describe()
            file.head()
            file.info()
            print(f"Shape of the dataset: {file.shape}")
            print(f"Number of missing values: {file.isnull().sum().sum()}")
            print(f"Number of unique values: \n {file.nunique()}")
            

            self.terminal_message=QDialog()
            self.terminal_message.setWindowTitle("Terminal")

            text_edit=QTextEdit()
            text_edit.setText("------------------ OVERVIEW OF THE DATASET -----------------")
            text_edit.append("This dataset gives us information about the heart attack risk of a person based on certain attributes about the persons health condition.")
            text_edit.append("The attributes are as follows: ")
            text_edit.append("1. Age\n 2.Gender\n 3.Chest Pain Type\n 4.Cholestoral\n 5.Resting Blood Pressure\n 6.Fasting Blood Sugar > 120 mg/dl\n 7.Resting Electrocardiographic Results\n 8.Exercise Induced Angina\n 9.ST Depression Induced By Exercise Relative To Rest\n 10.Maximum Heart Rate Achieved")
            text_edit.append(f"Shape of the dataset: {file.shape}")
            text_edit.append(f"Number of missing values: {file.isnull().sum().sum()}")
            text_edit.append(f"Number of unique values: \n {file.nunique()}")
            # Data description
            text_edit.append("------------------ DATA DESCRIPTION -----------------")
            text_edit.append(f"{file.describe()}")
            text_edit.append("-------------------------------------------------")
            
            text_edit.setReadOnly(True)

            layout=QVBoxLayout()
            layout.addWidget(text_edit)
            self.terminal_message.setLayout(layout)
            # Set initial size to 500x900 pixels
            self.terminal_message.resize(900, 500)
            self.terminal_message.exec()
            
            return True
        except:
            self.terminal_message=QDialog()
            self.terminal_message.setWindowTitle("Terminal")

            text_edit=QTextEdit()
            text_edit.setText("File not found or invalid file format!")
            text_edit.setReadOnly(True)

            layout=QVBoxLayout()
            layout.addWidget(text_edit)
            self.terminal_message.setLayout(layout)

            self.terminal_message.exec()
            
            return False


# Loading dialog
class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Running the model...")
        self.setFixedSize(200, 120)  # Set the fixed size of the dialog

        layout = QVBoxLayout(self)
        progress_bar = QProgressBar(self)
        progress_bar.setMinimum(0)
        progress_bar.setMaximum(100)
        layout.addWidget(progress_bar)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_progress(progress_bar))
        self.timer.start(50)  # Adjust the interval as needed


    def update_progress(self, progress_bar):
        current_value = progress_bar.value()
        new_value = (current_value + 1) % (progress_bar.maximum() + 1)
        progress_bar.setValue(new_value)

        if new_value == 100:
            self.timer.stop()
            self.close()

def main():
    app = QApplication([])
    widget = Widget()
    widget.show()
    app.exec()

if __name__ == "__main__":
    main()