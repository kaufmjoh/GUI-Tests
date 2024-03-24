import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import random




class ScatterPlotWindow(QMainWindow):
    #def __init__(self, dataframe1, dataframe2, dataframe3): #Make this part generic, take a single dataframe, where 1 column is the scattegory
    def __init__(self, dataframe): #Make this part generic, take a single dataframe, where 1 column is the scattegory
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 800, 600)
        


        grouped = dataframe.groupby('c') 

        self.dataframes = {}

        for name, group in grouped:
            self.dataframes[name] = group

        self.numPlots = len(self.dataframes)


        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.canvas = PlotCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)
        
        self.slider_label = QLabel("Select Scatter Plot:")
        layout.addWidget(self.slider_label)
        
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(self.numPlots)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.update_plot) #Call this function when the slider changes
        layout.addWidget(self.slider)
        
        self.plot_scatter(1)
        
    #Plot the scatter plot using matplotlib
    def plot_scatter(self, index):
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

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.figure = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)

if __name__ == '__main__':
    # Example DataFrames (replace these with your own dataframes)

    c = []
    x = []
    y = []

    #This many plots
    for i in range(0, 180):

        #This many x values
        for j in range(0, 10000):
            c.append(i)
            x.append(j)
            y.append(random.randint(1, 10000))


    df = pd.DataFrame( {'c':c, 'x':x, 'y':y} )
    
    print("Hardest part was generating the data")

    app = QApplication(sys.argv)
    window = ScatterPlotWindow(df)
    window.show()
    sys.exit(app.exec_())
