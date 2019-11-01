# coding=UTF-8
'''
SocketServer 支持多个客户端
'''
import socketserver
import _thread
import time
import struct
import base64
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import pythonSocketServer
import traceback
import cx_Oracle
import os
from util.util import strToFloat,bytesToHexString


class ClientSession():
  def __init__(self, address, serial, request):
     self.address=address
     self.serial = serial
     self.request = request


def clientHeart(ip, heart):
    if list:
        for i in range(len(list)):
            if list[i].address == ip:
                list[i].serial = heart

def dataSwitch(data):
    str1 = ''
    str2=bytes()
    data = data.replace(" ", "");
    while data:
        str1 = data[0:2]
        s = int(str1,16)
        str2 += struct.pack('B',s)
        data = data[2:]
    return str2


class ShowMessageWindow(QMainWindow,pythonSocketServer.Ui_MainWindow):
    _signal = pyqtSignal(str)
    def __init__(self):
        super(ShowMessageWindow,self).__init__()
        self.setupUi(self)
        self.init();
        self._signal.connect(self.showmessage)

        # self.startListenButton.clicked.connect(self.write)

    def collect(self):
        while True:
            if list:
                try:
                    time.sleep(5)
                    for i in range(len(list)):
                        print("序号：%s   %s" % (i, list[i].address))
                        print("对象心跳包为 %s 发送指令: %s " % (list[i].serial, cmd1))
                        self.showMessageInWindow("序号："+str(i)+" 发送指令："+ cmd1)
                        self.showMessageInWindow("对象心跳包为 " + str(list[i].serial)+" 发送指令: " + cmd1)
                        list[i].request.send(cmd);
                except Exception as e:
                    print("collect 客户端断开 %s" % e)
                    list.remove(list[i])
            time.sleep(1)


    def Listening(self):
        # server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler  #不支持多并发
        server = socketserver.ThreadingTCPServer((HOST, PORT), self.MyTCPHandler)  # 支持多线程，多并发
        # server = SocketServer.ForkingTCPServer((HOST, PORT), MyTCPHandler)  # 支持多进程，多并发，windows不能实现，linux上可以
        # server.allow_reuse_address() #解决 在 socketServer程序里面出现 地址已经被占用
        server.serve_forever()

    def showMessageInWindow(self, message):

        self._signal.emit(str(message))



    def showmessage(self, message):

        Str = self.textEdit.toPlainText()
        Str = Str + message + "\r\n"
        self.textEdit.setPlainText(Str)

    def init(self):
        _thread.start_new_thread(self.collect, ())
        _thread.start_new_thread(self.Listening, ())


    class MyTCPHandler(socketserver.BaseRequestHandler):
        '''
        处理我们的socket，这个类必须继承socketserver.BaseRequestHandler
        并且实现里面的handler函数
        '''

        def setup(self):
            print("这里处理请求前的的事情，也可以不写")
            win.showMessageInWindow("ip: " + str(self.client_address[0]) + " 端口：" + str(self.client_address[1]) + " 接入")
            x = ClientSession(self.client_address, "", self.request);
            list.append(x)
            pass

        def handle(self):

            '''处理客户端请求'''
            while self:
                try:
                    self.data = self.request.recv(1024).strip()
                    print("{} wrote:".format(self.client_address))  # 客户端地址
                    print(bytesToHexString(self.data))
                    ip = str(self.client_address[0])
                    resultStr = bytesToHexString(self.data)
                    # ShowMessageWindow.showMessageInWindow(ip + " 接收到信息: " + resultStr)  # 客户端地址
                    if len(resultStr) == 6:
                        print(self.client_address[0] + " 的心跳包为: " + resultStr)
                        clientHeart(self.client_address, resultStr)

                    # self.request.send(self.data.upper())

                except Exception as e:
                    print("MyTCPHandler 客户端断开 %s" % e)
                    break

        def finish(self):
            print("处理请求完成之后的事情，也可以不写")
            # ShowMessageWindow.showMessageInWindow("ip: " + str(self.client_address[0]) + " 端口：" + str(self.client_address[1]) + " 断开")
            pass


def oracleTest():
    conn = cx_Oracle.connect('kang/123456@192.168.8.163/orcl')  # 这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字
    cur = conn.cursor()
    sql = "SELECT * FROM DEMO"
    cur.execute(sql)
    rows = cur.fetchall()  # 得到所有数据集
    # cur.execute("INSERT INTO demo (ID, name)VALUES(2, 'asdfa')")
    cur.close()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'   #解决数据库查询乱码
    oracleTest()

    test=strToFloat("C3 9D 14 63")

    HOST, PORT = "0.0.0.0", 9999
    list = []
    cmd1 = "02 03 00 07 00 03 B4 39"  # 获取字符测
    cmd = dataSwitch(cmd1);
    win=ShowMessageWindow()
    win.show()

    sys.exit(app.exec_())











