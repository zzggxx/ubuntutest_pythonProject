import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow, self).__init__()
        self.setWindowTitle("the first windows")
        self.resize(300, 400)
        self.statusBar().showMessage("only five second,I will dismiss", 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = FirstMainWindow()
    main.show()
    sys.exit(app.exec_())
