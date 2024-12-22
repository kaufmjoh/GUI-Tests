import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QFileDialog
import os


class CombineCsvsWindow(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setWindowTitle('Scatter Plot')
        self.setGeometry(100, 100, 1600, 600)
        
        self.setup_ui()

    #Call the setup functions to setup the various layouts of the gui   
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

    #Setup the layout for where the output / results information will be stored
    def setupResultsBox(self):
        self.resultsLayout = QVBoxLayout()

        self.destinationFileName = QLabel("<Destination file name will appear here>")
        self.resultsLayout.addWidget(self.destinationFileName)


        #Button to allow the user to select the destination
        self.button = QPushButton(self)
        self.button.setFixedSize(200, 50)
        self.buttonLabel = QLabel("Select destination", self.button)
        self.button.clicked.connect(self.getDestinationFile)
        self.resultsLayout.addWidget(self.button, stretch=1)

        #When this button is pressed, it will run the combine csvs script
        self.button = QPushButton(self)
        self.button.setFixedSize(200, 50)
        self.buttonLabel = QLabel("Combine files", self.button)
        self.button.clicked.connect(self.runCombinationScript)
        self.resultsLayout.addWidget(self.button, stretch=1)

        self.centralLayout.addLayout(self.resultsLayout)

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

    def getDestinationFile(self):
        print("SUS!")
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setViewMode(QFileDialog.Detail)
            
        #dialog.setNameFilters(["Images (*.png *.xpm *.jpg)", "Text files (*.txt)", "All files (*)"])
        dialog.setNameFilters(["CSV Files (*.csv)"])
        if dialog.exec_():
            fileName = dialog.selectedFiles()[0]
            
            if not fileName.endswith(".csv"): #Add .csv to user's file name
                fileName += ".csv"
            
            self.destinationFileName.setText(fileName)
            print("Selected fileName", fileName)
        else:
            print("Failure question mark!")

    #Call the script to combine the csvs
    def runCombinationScript(self):

        batFileName = "combineCsvs.bat"
        cFileName = "combineCsvs.c"
        exeFileName = "combineCsvs.exe"
        inputFile1 = self.file1Name.text()
        inputFile2 = self.file2Name.text()
        outputFile = self.destinationFileName.text()

        cmd = batFileName + " " + cFileName + " " + exeFileName + " " + inputFile1 + " " + inputFile2 + " " + outputFile

        os.system(cmd)
        #os.system("combineCsvs.bat combineCsvs.c combineCsvs.exe data/ints.csv data/chars.csv data/combo.csv")

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = CombineCsvsWindow()
    window.show()
    sys.exit(app.exec_())
