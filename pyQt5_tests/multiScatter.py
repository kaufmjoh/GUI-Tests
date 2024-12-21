import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel, QPushButton, QLineEdit, QHBoxLayout
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random


WIDTH = 5
HEIGHT = 7


class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=WIDTH, height=HEIGHT, dpi=100):
        self.figure = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)

class ScatterPlotWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 1600, 600)
        
        self.sliderCreated = False
        self.setup_ui()

        
    def setup_ui(self):
        #Set up the central widget and the ui layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.layout = QVBoxLayout(centralWidget)

        self.canvas = PlotCanvas(self, width=WIDTH, height=HEIGHT)
        self.layout.addWidget(self.canvas)
        
        #This is the entry layout, which contrains the user input fields
        self.entryLayout = QHBoxLayout()

        #Setup a button that when pressed will generate the plots
        self.button = QPushButton(self)
        self.button.setFixedSize(100, 25)
        self.buttonLabel = QLabel("Generate Plots", self.button)
        self.button.clicked.connect(self.generatePlots)
        self.button.clicked.connect(self.createSlider)

        self.entryLayout.addWidget(self.button, stretch=1)

        #Setup a text input field that allows the user to choose how many plots to plot
        self.textEntry = QLineEdit()
        self.textEntryLabel = QLabel("Entered text")
        self.entryLayout.addWidget(self.textEntry)
        
        #Add the entryLayout to the main layout
        self.layout.addLayout(self.entryLayout)


    #Plot the scatter plot using matplotlib
    def plot_scatter(self, index):

        self.canvas.figure.clf()

        ax = self.canvas.figure.add_subplot()

        df = self.dataframes[index - 1]
        ax.scatter(df['x'], df['y'])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Scatter Plot {index}')

        self.canvas.draw()
    
    #Callback function that's called whenever the slider is updated
    def update_plot(self):
        index = self.slider.value()
        self.plot_scatter(index)

    #Generate the scatter plots
    def generatePlots(self):
        c = []
        x = []
        y = []

        #print("Generating Plots") #Why does this not print until after the window is closed?

        userTextEntry = self.textEntry.text()

        if userTextEntry == "":
            numPlots = 1
        else:
            numPlots = int(userTextEntry)

        #Generate numPlots number of plots
        for i in range(0, numPlots):

            #With these many (x, y) pairs
            for j in range(0, 1000):
                c.append(i)
                x.append(j)
                y.append(random.randint(1, 1000))


        df = pd.DataFrame( {'c':c, 'x':x, 'y':y} )
        
        grouped = df.groupby('c') 

        self.dataframes = {}

        for name, group in grouped:
            self.dataframes[name] = group

        self.numPlots = len(self.dataframes)
        
    #Create the slider element, which allows the user to select which plot to show
    def createSlider(self):
        if not self.sliderCreated:
            self.slider_label = QLabel("Select Scatter Plot:")
            self.layout.addWidget(self.slider_label)    
            self.slider = QSlider(Qt.Horizontal)
            self.slider.setTickPosition(QSlider.TicksBelow)
            self.slider.valueChanged.connect(self.update_plot) #Call this function when the slider changes

            # Set stretch factor for slider_label to make it smaller
            self.layout.addWidget(self.slider, stretch=1)
            self.layout.setStretchFactor(self.slider_label, 0)

            self.sliderCreated = True
    
        self.slider.setMinimum(1)
        self.slider.setMaximum(self.numPlots)
        self.slider.setTickInterval(1)      
        
        self.slider.setValue(1)
        self.plot_scatter(1) #Default plot to graph





if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = ScatterPlotWindow()
    window.show()
    sys.exit(app.exec_())
