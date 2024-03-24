import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class AdditionApp(QWidget):
    def __init__(self):
        super().__init__()

        # UI initialization
        self.init_ui()

    def init_ui(self):
        # Widgets
        self.num1_label = QLabel('Number 1:')
        self.num1_input = QLineEdit(self)

        self.num2_label = QLabel('Number 2:')
        self.num2_input = QLineEdit(self)

        self.result_label = QLabel('Result:')
        self.result_display = QLabel(self)

        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.clicked.connect(self.calculate_result)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('C Addition Program GUI')
        self.setGeometry(100, 100, 300, 200)

    def calculate_result(self):
        # Get input values
        num1 = int(self.num1_input.text())
        num2 = int(self.num2_input.text())

        # Perform addition
        result = num1 + num2

        # Display result
        self.result_display.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AdditionApp()
    window.show()
    sys.exit(app.exec_())