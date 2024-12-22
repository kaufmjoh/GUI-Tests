import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QFileDialog

WIDTH = 5
HEIGHT = 7

class CombineCsvsWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 1600, 600)
        
        self.setup_ui()

        
    def setup_ui(self):
        #Set up the central widget and the ui layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.centralLayout = QHBoxLayout(centralWidget)
        
        self.setupGetFile1Box()
        self.setupGetFile2Box()
        self.setupResultsBox()

    #Setup the layout for selecting the first csv file
    def setupGetFile1Box(self):
        #Setup a button to get the first csv file
        self.file1Layout = QVBoxLayout()

        self.file1Name = QLabel("<First file name will appear here>")
        self.file1Layout.addWidget(self.file1Name)

        self.button = QPushButton(self)
        self.button.setFixedSize(200, 50)
        self.buttonLabel = QLabel("Select first file for combination", self.button)
        self.button.clicked.connect(self.getFile1)
        self.file1Layout.addWidget(self.button, stretch=1)

        self.centralLayout.addLayout(self.file1Layout)

    #Setup the layout for selecting the second csv file
    def setupGetFile2Box(self):
        #Setup a button to get the second csv file
        self.file2Layout = QVBoxLayout()

        self.file2Name = QLabel("<Second file name will appear here>")
        self.file2Layout.addWidget(self.file2Name)

        self.button = QPushButton(self)
        self.button.setFixedSize(200, 50)
        self.buttonLabel = QLabel("Select second file for combination", self.button)
        self.button.clicked.connect(self.getFile2)
        self.file2Layout.addWidget(self.button, stretch=1)

        self.centralLayout.addLayout(self.file2Layout)

    #Setup the layout for where the results information will be stored
    def setupResultsBox(self):
        self.resultsLayout = QVBoxLayout()

        self.button = QPushButton(self)
        self.button.setFixedSize(200, 50)
        self.buttonLabel = QLabel("Combine files", self.button)
        self.button.clicked.connect(self.runCombinationScript)

    #Open the dialog to get the first csv file
    def getFile1(self):

        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            print("Selected file 1:", file_name)
            self.file1Name.setText(file_name)

    #Open the dialog to get the second csv file
    def getFile2(self):
    
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            print("Selected file 2:", file_name)
            self.file2Name.setText(file_name)

    #Call the script to combine the csvs
    def runCombinationScript(self):
        print("Mistakes were made")
        #Do some more stuff

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = CombineCsvsWindow()
    window.show()
    sys.exit(app.exec_())
