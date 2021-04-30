import sys
import untitled
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = untitled.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    print(ui.pushButton.sizeHint().width())
    print(ui.pushButton.sizeHint().height())
    ui.pushButton

    sys.exit(app.exec_())
