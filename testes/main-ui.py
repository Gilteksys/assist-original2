from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MainWindow")
        self.setGeometry(0, 0, 1125, 892)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout(main_widget)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        layout.addWidget(line)

        line_2 = QFrame()
        line_2.setFrameShape(QFrame.VLine)
        layout.addWidget(line_2)

        button_1 = QPushButton("PushButton 1")
        layout.addWidget(button_1)

        button_2 = QPushButton("PushButton 2")
        layout.addWidget(button_2)

        button_3 = QPushButton("PushButton 3")
        layout.addWidget(button_3)

        button_4 = QPushButton("PushButton 4")
        layout.addWidget(button_4)

        button_5 = QPushButton("PushButton 5")
        layout.addWidget(button_5)

        line_3 = QFrame()
        line_3.setFrameShape(QFrame.HLine)
        layout.addWidget(line_3)

        line_4 = QFrame()
        line_4.setFrameShape(QFrame.VLine)
        layout.addWidget(line_4)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()





