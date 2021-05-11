# coding=utf-8
# 默认的加入
import sys
# 将UI文件进行导入
import ubuntutest
# 是测试4G模块的包
import platform
import subprocess
# 串口测试 pip install pyserial
import serial
# 线程安全的包Timer
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


# ttyS0:485   ttyS1 ttyS2 ttyS3:232
mTestString = 'sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7f4s5d1f3a54w5r3eq4'


def onClick_Button_Serial():
    testStringLen = len(mTestString)
    ser0, isopen0 = open_Serial(9600, '/dev/ttySC0', 10)
    ser1, isopen1 = open_Serial(9600, '/dev/ttySC1', 10)
    if isopen0 and isopen1:
        ser0.write(mTestString)
        receivedata = ser1.read(testStringLen).decode()
        if receivedata in mTestString:
            ser0Write9600 = True
            ser1Read9600 = True
            print('----------')
        ser1.write(mTestString)
        receivedata = ser0.read(testStringLen).decode()
        if receivedata in mTestString:
            ser1Write9600 = True
            ser0Read9600 = True
            print('----------++++++++++')
        ser0.close()
        ser1.close()
'''
    ser0, isopen0 = open_Serial(115200, '/dev/ttySC0', 10)
    ser1, isopen1 = open_Serial(115200, '/dev/ttySC1', 10)
    if isopen0 and isopen1:
        ser0.write(mTestString)
        receivedata = ser1.read(testStringLen).decode()
        if receivedata in mTestString:
            ser0Write115200 = True
            ser1Read115200 = True
        ser1.write(mTestString)
        receivedata = ser0.read(testStringLen).decode()
        if receivedata in mTestString:
            ser1Write115200 = True
            ser0Read115200 = True
        ser0.close()
        ser1.close()

    if ser0Write9600 and ser0Write115200 and ser0Read9600 and ser0Read115200:
        ser0 = True
        print('the serial port is right: %s' % ser0)
    if ser1Write9600 and ser1Write115200 and ser1Read9600 and ser1Read115200:
        ser1 = True
        print('the serial port is right: %s' % ser1)
'''


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
