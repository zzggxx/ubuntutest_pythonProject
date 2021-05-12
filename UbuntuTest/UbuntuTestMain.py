#coding=utf-8
import platform
import sys
import ubuntutest
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

def onClick_Button_Ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    isRight4G = subprocess.call(command, 10) == 0
    if isRight4G:
        ui.label.setText('true')
    else:
        ui.label.setText('false')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = ubuntutest.Ui_MainWindow()
    ui.setupUi(mainWindow)

    ui.pushButton.clicked.connect(lambda: onClick_Button_Ping('www.baidu.com'))

    mainWindow.show()

    hanshu = lambda x,y:x+y;
    print(hanshu(1, 2))

    sys.exit(app.exec_())