import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ScatterPlotWindow(QMainWindow):
    def __init__(self, dataframe):
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 800, 600)
        
        self.dataframe = dataframe
        
        self.setup_ui()
        
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.canvas = PlotCanvas(self, width=5, height=4)
        layout.addWidget(self.canvas)
        
        self.plot_scatter()
        
    def plot_scatter(self):
        ax = self.canvas.figure.add_subplot(111)
        ax.scatter(self.dataframe['x'], self.dataframe['y'])
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Scatter Plot')
        self.canvas.draw()

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.figure = plt.figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)

if __name__ == '__main__':
    # Example DataFrame (replace this with your own data)
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [5, 4, 3, 2, 1]
    }
    df = pd.DataFrame(data)
    
    app = QApplication(sys.argv)
    window = ScatterPlotWindow(df)
    window.show()
    sys.exit(app.exec_())
