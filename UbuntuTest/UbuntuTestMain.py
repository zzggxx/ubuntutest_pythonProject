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
mTestString = 'sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegf' \
              'jsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqsd' \
              'faeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjs' \
              'gerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksd' \
              'b641231231564867465135468e7f4s5d1f3a54w5r3eqsdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78tey' \
              'iYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwe' \
              'tygfuiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7f4s5d1f3a54w5r3eq4sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSb' \
              'fkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasgu' \
              'ywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7f4s5d1f3a54w5r3eq4sdfaeoifyalfhalieyrilah' \
              'lfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguy' \
              'fbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7fsdfaeoif' \
              'yalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuy' \
              'ctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7f4s5d1' \
              'sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbj' \
              'xuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb6sdfaeoifyalfhalieyrilahlfaye' \
              'rgjdghfkjvgJHSbfkjawetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtf' \
              'uwgyejhasguywdfegyrfuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb64123123156sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkj' \
              'awetgywegrfweyrt78teyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyr' \
              'fuysgdjvcuwetygfuiwgehflhaeuirtypqeyteluhdfjksdb6412312sdfaeoifyalfhalieyrilahlfayergjdghfkjvgJHSbfkjawetgywegrfweyrt78t' \
              'eyiYQuiwhwlefhluewgrfffffdhbvxhcgfuegfjsbdcjsgerytfwuehfzbjxuyctweguyfbjhxdtguyebceywtfuwgyejhasguywdfegyrfuysgdjvcuwetygf' \
              'uiwgehflhaeuirtypqeyteluhdfjksdb641231231564867465135468e7f4s5d1f3a54w5r3eq431564867465135468e7f4s5d1f3a54w5r3eq44867465135' \
              '468e7f4s5d1f3a54w5r3eq441231231564867465135468e7f4s5d1f3a54w5r3eq4f3a54w5r3eq44s5d1f3a54w5r3eq44eyteluhdfjksdb64123123156486' \
              '7465135468e7f4s5d1f3a54w5r3eq4'


def onClick_Button_Serial():
    testStringLen = len(mTestString)

    ser0Write9600 = False
    ser1Read9600 = False
    ser1Write9600 = False
    ser0Read9600 = False
    ser0Write115200 = False
    ser1Read115200 = False
    ser1Write115200 = False
    ser0Read115200 = False

    ser2Write9600 = False
    ser3Read9600 = False
    ser3Write9600 = False
    ser2Read9600 = False
    ser2Write115200 = False
    ser3Read115200 = False
    ser3Write115200 = False
    ser2Read115200 = False

    ser0, isopen0 = open_Serial(9600, '/dev/ttyS0', 5)
    ser1, isopen1 = open_Serial(9600, '/dev/ttyS1', 5)
    if isopen0 and isopen1:
        ser0.write(mTestString.encode())
        receivedata10 = ser1.read(testStringLen).decode()
        if mTestString in receivedata10:
            ser0Write9600 = True
            ser1Read9600 = True
        ser1.write(mTestString.encode())
        receivedata00 = ser0.read(testStringLen).decode()
        if mTestString in receivedata00:
            ser1Write9600 = True
            ser0Read9600 = True
        ser0.close()
        ser1.close()

    ser0, isopen0 = open_Serial(115200, '/dev/ttyS0', 5)
    ser1, isopen1 = open_Serial(115200, '/dev/ttyS1', 5)
    if isopen0 and isopen1:
        ser0.write(mTestString.encode())
        receivedata11 = ser1.read(testStringLen).decode()
        if mTestString in receivedata11:
            ser0Write115200 = True
            ser1Read115200 = True
        ser1.write(mTestString.encode())
        receivedata01 = ser0.read(testStringLen).decode()
        if mTestString in receivedata01:
            ser1Write115200 = True
            ser0Read115200 = True
        ser0.close()
        ser1.close()

    if ser0Write9600 and ser0Write115200 and ser0Read9600 and ser0Read115200:
        ser0 = True
    else:
        ser0 = False
    print('the serial0 port is : %s' % ser0)
    if ser1Write9600 and ser1Write115200 and ser1Read9600 and ser1Read115200:
        ser1 = True
    else:
        ser1 = False
    print('the serial1 port is : %s' % ser1)

    ser2, isopen2 = open_Serial(9600, '/dev/ttyS2', 5)
    ser3, isopen3 = open_Serial(9600, '/dev/ttyS3', 5)
    if isopen2 and isopen3:
        ser2.write(mTestString.encode())
        receivedata30 = ser3.read(testStringLen).decode()
        if mTestString in receivedata30:
            ser2Write9600 = True
            ser3Read9600 = True
        ser3.write(mTestString.encode())
        receivedata20 = ser2.read(testStringLen).decode()
        if mTestString in receivedata20:
            ser3Write9600 = True
            ser2Read9600 = True
        ser2.close()
        ser3.close()

    ser2, isopen2 = open_Serial(115200, '/dev/ttyS2', 5)
    ser3, isopen3 = open_Serial(115200, '/dev/ttyS3', 5)
    if isopen2 and isopen3:
        ser2.write(mTestString.encode())
        receivedata31 = ser3.read(testStringLen).decode()
        if mTestString in receivedata31:
            ser2Write115200 = True
            ser3Read115200 = True
        ser3.write(mTestString.encode())
        receivedata21 = ser2.read(testStringLen).decode()
        if mTestString in receivedata21:
            ser3Write115200 = True
            ser2Read115200 = True
        ser2.close()
        ser3.close()

    if ser2Write9600 and ser2Write115200 and ser2Read9600 and ser2Read115200:
        ser2 = True
    else:
        ser2 = False
    print('the serial2 port is : %s' % ser2)

    if ser3Write9600 and ser3Write115200 and ser3Read9600 and ser3Read115200:
        ser3 = True
    else:
        ser3 = False
    print('the serial3 port is : %s' % ser3)

    if ser0 and ser1 and ser2 and ser3:
        result = 'success'
    else:
        result = 'failed'
    ui.label_2.setText(result)


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
