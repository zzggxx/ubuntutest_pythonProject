# coding=utf-8
# 默认的加入
import sys
# 将UI文件进行导入
import ubuntutest
# 是测试4G模块的包
import platform
import subprocess
# 串口测试
import serial
#
from threading import Timer

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


def onClick_Button_Ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    isRight4G = subprocess.call(command, 10) == 0
    if isRight4G:
        ui.label.setText('true')
    else:
        ui.label.setText('false')


def open_Serial(baudrate, port, timeout):
    ser = serial.Serial()
    ser.baudrate = baudrate
    ser.port = port
    ser.timeout = timeout
    ser.open()
    return ser, ser.is_open;


def onClick_Button_Serial():
    ser0, isopen0 = open_Serial(9600, '/dev/ttySC0', 10)
    ser1, isopen1 = open_Serial(9600, '/dev/ttySC1', 10)
    if isopen0 and isopen1:
        Timer(1, ser1.write('abcdefg')).start()
        recv = []
        while True:
            if ser0.in_waiting:
                r = ser0.read()
                if r != None:
                    recv.append(r)
                    print(recv)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = ubuntutest.Ui_MainWindow()
    ui.setupUi(mainWindow)

    # ping执行
    ui.pushButton.clicked.connect(lambda: onClick_Button_Ping('www.baidu.com'))
    # serial port test
    ui.pushButton_2.clicked.connect(lambda: onClick_Button_Serial())

    mainWindow.show()

    sys.exit(app.exec_())
