import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel, QPushButton
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random


WIDTH = 5
HEIGHT = 7


class ScatterPlotWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 1600, 600)
        
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)
        
        self.canvas = PlotCanvas(self, width=WIDTH, height=HEIGHT)
        self.layout.addWidget(self.canvas)
        
        #Setup a button that when pressed will generate the plots
        self.button = QPushButton(self)
        self.button.setFixedSize(150, 150)
        self.buttonLabel = QLabel("Generate Plots", self.button)
        self.button.clicked.connect(self.generatePlots)
        self.layout.addWidget(self.button, stretch=1)


        
    #Plot the scatter plot using matplotlib
    def plot_scatter(self, index):

        axs = self.canvas.figure.clf()

        ax = self.canvas.figure.add_subplot(111)


        df = self.dataframes[index - 1]
        ax.scatter(df['x'], df['y'])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Scatter Plot {index}')

        self.canvas.draw()
    
    #Callback function
    def update_plot(self):
        index = self.slider.value()
        self.plot_scatter(index)

    def generatePlots(self):
        c = []
        x = []
        y = []

        print("Generating Plots") #Why does this not print until after the window is closed?

        #This many plots
        for i in range(0, 90):

            #This many x values
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
        

        self.slider_label = QLabel("Select Scatter Plot:")
        self.layout.addWidget(self.slider_label)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(self.numPlots)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.update_plot) #Call this function when the slider changes
        
        
        # Set stretch factor for slider_label to make it smaller
        self.layout.addWidget(self.slider, stretch=1)
        self.layout.setStretchFactor(self.slider_label, 0)
        
        self.plot_scatter(1) #Default plot to graph




class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=WIDTH, height=HEIGHT, dpi=100):
        self.figure = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = ScatterPlotWindow()
    window.show()
    sys.exit(app.exec_())
