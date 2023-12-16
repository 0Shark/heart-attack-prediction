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


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QGridLayout, QSlider, QHBoxLayout
from PyQt6.QtCore import Qt
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

        # Create and add buttons to the layout
        self.label_gender = QLabel("Gender")

        # Create a horizontal layout for the gender buttons
        button_layout = QHBoxLayout()

        self.button_male = QPushButton("Male")
        self.button_female = QPushButton("Female")

        # Add buttons to the horizontal layout
        button_layout.addWidget(self.button_male)
        button_layout.addWidget(self.button_female)

        # Create and add other widgets to the layout
        self.label_age = QLabel("Age")
        self.slider_age = QSlider(Qt.Orientation.Horizontal)
        self.slider_age.setMaximumWidth(150)
        self.slider_age.setMinimum(29)
        self.slider_age.setMaximum(77)
        self.slider_age.setValue(53)
        self.slider_age.setTickInterval(1)
        self.slider_age.valueChanged.connect(self.value_changed)
        self.label_slider_age = QLabel("Age: " + str(self.slider_age.value()))

        # Add widgets to the grid layout
        grid_layout.addWidget(self.label_gender, 0, 0)
        grid_layout.addLayout(button_layout, 1, 0)  # Add the button layout to the same row
        grid_layout.addWidget(self.label_age, 2, 0)
        grid_layout.addWidget(self.slider_age, 3, 0)
        grid_layout.addWidget(self.label_slider_age, 3, 1)


        # Set the layout for the home tab
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

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    app.exec()
