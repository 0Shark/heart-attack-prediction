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
# dataset 1: https://www.kaggle.com/datasets/jeremylarcher/american-house-prices-and-demographics-of-top-cities/code
# dataset 2: https://www.kaggle.com/datasets/adampq/air-quality-index-by-state-1980-2022

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget
from PyQt6.QtCore import Qt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recommendation System")
        self.resize(750, 550)

    def buttons(self):
        self.button1 = QPushButton("Button 1")
        self.button2 = QPushButton("Button 2")
        self.button3 = QPushButton("Button 3")

        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

    def tabs_section(self):
        tabs = QTabWidget(self)
        tabs.setTabPosition(QTabWidget.TabPosition.North)
        tabs.setMovable(True)

        # Show all tabs without arrow buttons
        tabs.setDocumentMode(True)

        tab1 = QWidget()
        tab2 = QWidget()

        tabs.addTab(tab1, "Home")
        tabs.addTab(tab2, "Visualisation")
        tabs.setMinimumWidth(200)
        # Set elide mode for tab text (adjust as needed)
        tabs.setElideMode(Qt.TextElideMode.ElideRight)

if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.buttons()
    widget.tabs_section()
    widget.show()
    app.exec()
