from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget, QLabel, QGridLayout, QSlider, QHBoxLayout, QSpinBox, QDial, QProgressBar, QDialog, QFileDialog, QLineEdit, QTextEdit, QCheckBox, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from model import Model

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Heart Attack Risk Calculator")
        self.resize(750, 550)
        self.tabs_section()        
        self.tabs.setCurrentIndex(0)
        self.setWindowIcon(QIcon("heart.png"))
        self.display_home()
        self.model = False

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
        self.st_depression_induced_by_exercise_relative_to_rest_label = QLabel("ST Depression Induced By\n Exercise Relative To Rest: " + str(self.st_depression_induced_by_exercise_relative_to_rest.value()))
        
        # slope of the peak exercise ST segment
        # 0: upsloping
        # 1: flat
        # 2: downsloping
        self.slope_of_the_peak_exercise_ST_segment = QSpinBox()
        self.slope_of_the_peak_exercise_ST_segment.setMinimumWidth(120)
        self.slope_of_the_peak_exercise_ST_segment.setMaximumWidth(120)
        self.slope_of_the_peak_exercise_ST_segment.setMinimum(0)
        self.slope_of_the_peak_exercise_ST_segment.setMaximum(2)
        self.slope_of_the_peak_exercise_ST_segment.setValue(0)
        self.slope_of_the_peak_exercise_ST_segment.setSingleStep(1)
        self.slope_of_the_peak_exercise_ST_segment.valueChanged.connect(self.value_changed)
        self.slope_of_the_peak_exercise_ST_segment_label = QLabel("Slope Of The Peak\n Exercise ST Segment: " + str(self.slope_of_the_peak_exercise_ST_segment.value()))
        
        # CA 
        # number of major vessels (0-3) colored by flourosopy
        # 0: 0
        # 1: 1
        # 2: 2
        # 3: 3
        self.ca = QSpinBox()
        self.ca.setMinimumWidth(120)
        self.ca.setMaximumWidth(120)
        self.ca.setMinimum(0)
        self.ca.setMaximum(3)
        self.ca.setValue(0)
        self.ca.setSingleStep(1)
        self.ca.valueChanged.connect(self.value_changed)
        self.ca_label = QLabel("CA\n(number of major vessels\n (0-3) colored by flourosopy): " + str(self.ca.value()))
        
        # Thal 0 = normal; 1 = fixed defect; 2 = reversable defect
        self.thal = QSpinBox()
        self.thal.setMinimumWidth(120)
        self.thal.setMaximumWidth(120)
        self.thal.setMinimum(0)
        self.thal.setMaximum(2)
        self.thal.setValue(0)
        self.thal.setSingleStep(1)
        self.thal.valueChanged.connect(self.value_changed)
        self.thal_label = QLabel("Thal\n0 = normal\n1 = fixed defect\n2 = reversable defect")
        
        # select label
        self.btn_open_dialog = QPushButton('Select File', self)
        self.btn_open_dialog.setMaximumWidth(90)
        self.btn_open_dialog.clicked.connect(self.show_file_dialog)

        self.textbox_file_path = QLineEdit(self)
        self.textbox_file_path.setMaximumWidth(200)
        self.textbox_file_path.setReadOnly(True)
        self.textbox_file_path.setText("No file selected")

        # Result label
        self.result_label = QLabel("Result:")
        

        # Calculate heart attack risk
        go_button = QPushButton("Train")
        go_button.setMaximumWidth(80)
        go_button.clicked.connect(self.train)
        
        # Predict
        predict_button = QPushButton("Predict")
        predict_button.setMaximumWidth(80)
        predict_button.clicked.connect(self.predict)
        
        # Gender
        grid_layout.addWidget(self.gender_label, 0, 0)
        grid_layout.addWidget(self.gender_label, 0, 0)
        grid_layout.addWidget(self.male_radio, 1, 0)
        grid_layout.addWidget(self.female_radio, 1, 1)

        # Age slider
        grid_layout.addWidget(self.label_slider_age, 2, 0)
        grid_layout.addWidget(self.slider_age, 3, 0, 1, 2)

        # Resting blood pressure
        grid_layout.addWidget(self.resting_blood_pressure_label, 5, 0)
        grid_layout.addWidget(self.resting_blood_pressure, 6, 0)
        
        # Resting electrocardiographic results
        grid_layout.addWidget(self.resting_electrocardiographic_results_label, 4, 2)
        grid_layout.addWidget(self.resting_electrocardiographic_results, 5, 2)

        # Chest pain type
        grid_layout.addWidget(self.chest_pain_type_label, 7, 0)
        grid_layout.addWidget(self.chest_pain_type, 8, 0)
        
        # Fasting blood sugar
        grid_layout.addWidget(self.fasting_blood_sugar, 9, 0)
        
        # Exercise induced angina
        grid_layout.addWidget(self.exercise_induced_angina, 10, 0)
        
        # ST depression induced by exercise relative to rest
        grid_layout.addWidget(self.st_depression_induced_by_exercise_relative_to_rest_label, 6, 2)
        grid_layout.addWidget(self.st_depression_induced_by_exercise_relative_to_rest, 7, 2)

        # CA number of major vessels (0-3) colored by flourosopy
        grid_layout.addWidget(self.ca_label, 0, 2)
        grid_layout.addWidget(self.ca, 1, 2)

        # Cholestoral dial
        grid_layout.addWidget(self.cholestoral_dial_label, 2, 2)
        grid_layout.addWidget(self.cholestoral_dial, 3, 2)
        
        # Maximum heart rate achieved
        grid_layout.addWidget(self.maximum_heart_rate_achieved_label, 8, 2)
        grid_layout.addWidget(self.maximum_heart_rate_achieved, 9, 2)
        
        # Slope of the peak exercise ST segment
        grid_layout.addWidget(self.slope_of_the_peak_exercise_ST_segment_label, 11, 0)
        grid_layout.addWidget(self.slope_of_the_peak_exercise_ST_segment, 12, 0)
        
        # Thal 0 = normal; 1 = fixed defect; 2 = reversable defect
        grid_layout.addWidget(self.thal_label, 13, 0)
        grid_layout.addWidget(self.thal, 14, 0)
        
        #result label
        grid_layout.addWidget(self.result_label, 11, 2)
        #predict button
        grid_layout.addWidget(predict_button, 11, 3)
        #file path
        grid_layout.addWidget(self.btn_open_dialog, 12, 3)
        grid_layout.addWidget(self.textbox_file_path, 12, 2)
        #go button
        grid_layout.addWidget(go_button, 13, 2)

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
        try:
            self.file=pd.read_csv(self.textbox_file_path.text())
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
            return
        # Create a widget for the visualization tab
        visualization_tab_widget = QWidget()
        self.layout = QGridLayout(visualization_tab_widget)
        self.figure1 = Figure()
        self.canvas1 = FigureCanvas(self.figure1)
        self.layout.addWidget(self.canvas1, 0, 0)  # Add canvas1 to the top-left position (0, 0)

        self.figure2 = Figure()
        self.canvas2 = FigureCanvas(self.figure2)
        self.layout.addWidget(self.canvas2, 0, 1)  # Add canvas2 to the top-right position (0, 1)

        # Create labels or other widgets below the canvas widgets
        label1 = QLabel(f"The average age is {self.file['age'].mean():.2f} years old.")
        self.layout.addWidget(label1, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)  # Add label1 below canvas1

        label2 = QLabel(f"The average cholestoral is {self.file['chol'].mean():.2f} mg/dl.")
        self.layout.addWidget(label2, 1, 1, alignment=Qt.AlignmentFlag.AlignHCenter)  # Add label2 below canvas2

        label3= QLabel(f"The average maximum heart rate achieved is {self.file['thalach'].mean():.2f} bpm.")
        self.layout.addWidget(label3, 2, 0, alignment=Qt.AlignmentFlag.AlignHCenter)  # Add label3 below canvas1
        # Set some spacing between widgets
        self.layout.setSpacing(20)

        self.plot_data1()  # Plot data on canvas1
        self.plot_data2()  # Plot data on canvas2

        self.tabs.widget(1).setLayout(QVBoxLayout(self.tabs.widget(1)))
        self.tabs.widget(1).layout().addWidget(visualization_tab_widget)

    def plot_data1(self):
        
        ax = self.figure1.add_subplot(111)
        #get 1 point from the input
        try:
            age_point= int(self.slider_age.value())
            chol_point= int(self.cholestoral_dial.value())
        except:
            self.terminal_message=QDialog()
            self.terminal_message.setWindowTitle("Terminal")

            text_edit=QTextEdit()
            text_edit.setText("Please Enter Valid Values for Age and Cholestoral!")
            text_edit.setReadOnly(True)

            layout=QVBoxLayout()
            layout.addWidget(text_edit)
            self.terminal_message.setLayout(layout)

            self.terminal_message.exec()
            return


        x = self.file["age"] + age_point
        y = self.file["chol"] + chol_point

        # Assign colors based on age (just an example, customize based on your needs)
        colors = np.where(x < 40, 'red', np.where((40 <= x) & (x < 50), 'green', 'blue'))
        colors[-1]="black"
        ax.scatter(x, y, c=colors, marker='o')
        ax.set_title('Cholestoral vs Age')
        ax.set_xlabel('Age')
        ax.set_ylabel('Cholestoral')

        # Trigger canvas update
        self.canvas1.draw()

        self.tabs.widget(1).setLayout(QVBoxLayout(self.tabs.widget(1)))
        self.tabs.widget(1).layout().addWidget(self.canvas1)
    
    def plot_data2(self):
        ax = self.figure2.add_subplot(111)
        plt.style.use('_mpl-gallery-nogrid')
        x= self.file["age"]
        y= self.file["thalach"]
        ax.hist2d(x, y, bins=20, cmap='Reds')
        ax.set_title('Maximum Heart Rate Achieved vs Age')
        ax.set_xlabel('Age')
        ax.set_ylabel('Maximum Heart Rate Achieved')
        self.canvas2.draw()
        self.tabs.widget(1).setLayout(QVBoxLayout(self.tabs.widget(1)))
        self.tabs.widget(1).layout().addWidget(self.canvas2)



    def value_changed(self):
        self.label_slider_age.setText("Age: " + str(self.slider_age.value()))
        self.chest_pain_type_label.setText("Chest Pain Type: " + str(self.chest_pain_type.value()))
        self.cholestoral_dial_label.setText("Cholestoral: " + str(self.cholestoral_dial.value()))
        self.resting_blood_pressure_label.setText("Resting Blood Pressure: " + str(self.resting_blood_pressure.value()))
        self.resting_electrocardiographic_results_label.setText("Resting Electrocardiographic Results: " + str(self.resting_electrocardiographic_results.value()))
        self.st_depression_induced_by_exercise_relative_to_rest_label.setText("ST Depression Induced\n By Exercise Relative To Rest: " + str(self.st_depression_induced_by_exercise_relative_to_rest.value()))
        self.maximum_heart_rate_achieved_label.setText("Maximum Heart Rate Achieved: " + str(self.maximum_heart_rate_achieved.value()))
        self.slope_of_the_peak_exercise_ST_segment_label.setText("Slope Of The Peak\n Exercise ST Segment: " + str(self.slope_of_the_peak_exercise_ST_segment.value()))
        self.ca_label.setText("CA\n(number of major vessels\n (0-3) colored by flourosopy): " + str(self.ca.value()))
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
        print(f"Slope Of The Peak Exercise ST Segment: {self.slope_of_the_peak_exercise_ST_segment.value()}")
        print(f"CA (number of major vessels (0-3) colored by flourosopy): {self.ca.value()}")
        print(f"Thal (0 = normal; 1 = fixed defect; 2 = reversable defect): {self.thal.value()}")
        print("-------------------------------------------------")
        
        
    def train(self):
        if self.check_dataset():
            progress_dialog = ProgressDialog(self)
            progress_dialog.exec()
            self.model = Model(self.textbox_file_path.text())
            self.model.model_training()
    
    
    def predict(self):
        if self.model:
            # Get all input values
            age = int(self.slider_age.value())
            gender = self.gender_group.checkedButton().text()
            if gender == "Male":
                gender = 1
            else:
                gender = 0
            cp = int(self.chest_pain_type.value())
            trestbps = int(self.resting_blood_pressure.value())
            chol = int(self.cholestoral_dial.value())
            fbs = int(self.fasting_blood_sugar.isChecked())
            restecg = int(self.resting_electrocardiographic_results.value())
            exang = int(self.exercise_induced_angina.isChecked())
            oldpeak = int(self.st_depression_induced_by_exercise_relative_to_rest.value())
            thalach = int(self.maximum_heart_rate_achieved.value())
            slope = int(self.slope_of_the_peak_exercise_ST_segment.value())
            ca = int(self.ca.value())
            thal = int(self.thal.value())
            
            # Predict
            prediction = self.model.predict([age, gender, cp, trestbps, chol, fbs, restecg, exang, oldpeak, thalach, slope, ca, thal])[0]
            # Show result
            self.result_label.setText("Result: " + str(prediction))
        else:
            self.terminal_message=QDialog()
            self.terminal_message.setWindowTitle("Terminal")

            text_edit=QTextEdit()
            text_edit.setText("Model not trained!")
            text_edit.setReadOnly(True)

            layout=QVBoxLayout()
            layout.addWidget(text_edit)
            self.terminal_message.setLayout(layout)

            self.terminal_message.exec()
    
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