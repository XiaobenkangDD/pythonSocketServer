# coding=UTF-8
'''
SocketServer 支持多个客户端
'''
import SocketServer
import thread
import time
import struct


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
    str2 = ''
    data = data.replace(" ", "");
    while data:
        str1 = data[0:2]
        s = int(str1,16)
        str2 += struct.pack('B',s)
        data = data[2:]
    return str2

class MyTCPHandler(SocketServer.BaseRequestHandler):
    '''
    处理我们的socket，这个类必须继承socketserver.BaseRequestHandler
    并且实现里面的handler函数
    '''
    def setup(self):
        print("这里处理请求前的的事情，也可以不写")
        x=ClientSession(self.client_address, "" , self.request);
        list.append(x)
        pass

    def handle(self):
        '''处理客户端请求'''
        while self:
            try:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address))  # 客户端地址
                print(self.data.encode('hex'))
                resultStr=self.data.encode('hex')
                if len(resultStr) == 6:
                    print(self.client_address[0]+" 的心跳包为: "+resultStr)
                    clientHeart(self.client_address,resultStr)
                self.request.send(self.data.upper())
            except Exception as e:
                print("MyTCPHandler 客户端断开 %s" %e)
                break

    def finish(self):
        print("处理请求完成之后的事情，也可以不写")
        pass


def collect():
    while True:
        if list:
            time.sleep(5)
            for i in range(len(list)):
                try:
                   print ("序号：%s   %s" % (i,list[i].address))
                   print("对象心跳包为 %s 发送指令: %s " %(list[i].serial , cmd1) )
                   list[i].request.send(cmd);
                except Exception as e:
                    print("collect 客户端断开 %s" %e)
                    list.remove(list[i])
                    break



if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 9999
    list = []
    cmd1 = "02 03 00 07 00 03 B4 39"  # 获取字符测
    cmd = dataSwitch(cmd1);
    thread.start_new_thread(collect, ())
    # server = SocketServer.TCPServer((HOST,PORT),MyTCPHandler  #不支持多并发
    server = SocketServer.ThreadingTCPServer((HOST, PORT), MyTCPHandler)  # 支持多线程，多并发
    # server = SocketServer.ForkingTCPServer((HOST, PORT), MyTCPHandler)  # 支持多进程，多并发，windows不能实现，linux上可以
    # server.allow_reuse_address() #解决 在 socketServer程序里面出现 地址已经被占用
    server.serve_forever()









