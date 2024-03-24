import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSlider, QLabel
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ScatterPlotWindow(QMainWindow):
    def __init__(self, dataframe1, dataframe2, dataframe3):
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 800, 600)
        
        self.dataframes = [dataframe1, dataframe2, dataframe3]
        
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
        self.slider.setMaximum(3)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.update_plot)
        layout.addWidget(self.slider)
        
        self.plot_scatter(1)
        
    def plot_scatter(self, index):
        ax = self.canvas.figure.add_subplot(111)
        df = self.dataframes[index - 1]
        ax.scatter(df['x'], df['y'])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(f'Scatter Plot {index}')
        self.canvas.draw()
        
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
    data1 = {'x': [1, 2, 3, 4, 5], 'y': [1, 2, 3, 4, 5]}
    data2 = {'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1]}
    data3 = {'x': [1, 2, 3, 4, 5], 'y': [1, 4, 3, 2, 5]}
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    
    app = QApplication(sys.argv)
    window = ScatterPlotWindow(df1, df2, df3)
    window.show()
    sys.exit(app.exec_())
