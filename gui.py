'''
ou may also use other metrics or diagrams to do this.
• Create several input widgets (at least 3, where 2 must be different) that change some feature variables.
• A Scikit training model algorithm (e.g. from Aurélien Géron, Chapter 4) must be applied.
• Create 1 or 2 output canvas, i.e. for data visualization
• At least 3 statistical metrics over the input data must be shown
• The app must react interactively to the change of input parameter with a new prediction with visual-
ization.
1

'''
# dataset 1: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset/
# might help us: https://www.kaggle.com/code/nareshbhat/heart-attack-prediction-using-different-ml-models/notebook


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QGridLayout, QSlider, QHBoxLayout, QSpinBox, QDial, QProgressBar, QMessageBox, QDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recommendation System")
        self.resize(750, 550)
        self.tabs_section()        
        self.tabs.setCurrentIndex(0)
        self.setWindowIcon(QIcon("heart.png"))


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

       
        self.label_gender = QLabel("Gender")
        # Create a horizontal layout for the gender buttons
        button_layout = QHBoxLayout()
        self.button_male = QPushButton("Male")
        self.button_male.setMaximumWidth(80)
        self.button_female = QPushButton("Female")
        self.button_female.setMaximumWidth(80)

        # Add buttons to the horizontal layout
        button_layout.addWidget(self.button_male)
        button_layout.addWidget(self.button_female)

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
         # Update the alignment to AlignLeft
        
        #resting blood pressure
        self.resting_blood_pressure=QSpinBox()
        self.resting_blood_pressure.setMinimumWidth(120)
        self.resting_blood_pressure.setMaximumWidth(120)
        self.resting_blood_pressure.setMinimum(94)
        self.resting_blood_pressure.setMaximum(200)
        self.resting_blood_pressure.setValue(120)
        self.resting_blood_pressure.setSingleStep(1)
        self.slider_age.valueChanged.connect(self.value_changed)
        self.resting_blood_pressure_label = QLabel("Resting Blood Pressure: " + str(self.resting_blood_pressure.value()))
        self.resting_blood_pressure.valueChanged.connect(self.value_changed)

        
        # Result label
        result_label = QLabel("Result:")
        

        # Calculate heart attack risk
        go_button = QPushButton("GO")
        go_button.setMaximumWidth(80)
        go_button.clicked.connect(self.pop_up)
        grid_layout.addWidget(go_button, 9, 2)

        grid_layout.addWidget(self.label_gender, 0, 0)
        grid_layout.addLayout(button_layout, 1, 0)  # Add the button layout to the same row

        # Age slider
        grid_layout.addWidget(self.label_slider_age, 2, 0)
        grid_layout.addWidget(self.slider_age, 3, 0, 1, 2)

        # Resting blood pressure
        grid_layout.addWidget(self.resting_blood_pressure_label, 4, 0)
        grid_layout.addWidget(self.resting_blood_pressure, 5, 0)

        # Chest pain type
        grid_layout.addWidget(self.chest_pain_type_label, 6, 0)
        grid_layout.addWidget(self.chest_pain_type, 7, 0)

        # Cholestoral dial
        grid_layout.addWidget(self.cholestoral_dial_label, 0, 2)
        grid_layout.addWidget(self.cholestoral_dial, 1, 2)

        #result label
        grid_layout.addWidget(result_label, 8, 2)
        grid_layout.addWidget(go_button, 9, 2)

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
    
    def pop_up(self):
        progress_dialog = ProgressDialog(self)
        progress_dialog.exec()
        

    def update_progress(self, progress_bar, timer):
        current_value = progress_bar.value()
        new_value = (current_value + 1) % (progress_bar.maximum() + 1)
        progress_bar.setValue(new_value)

        if new_value == 0:
            timer.stop()

    def calculate_heart_attack_risk(self):
        pass

# MOS E PREK ME DOR IKYT KLASE !!

class ProgressDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Loading")
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

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    app.exec()
