'''
实验名称：Socket通信
版本： v1.0
日期： 2020.3
作者： 01Studio
说明：跟电脑网络助手进行Socket通信
社区：www.01studio.org
'''
import socket
import time

#构建socket对象s
s=socket.socket()

addr=('192.168.1.111',10000)
s.connect(addr)

#发送测试
s.send(b'Hello 01Studio!')

while True:
    
    text=s.recv(128) #单次最多接收128字节数据
    
    #接收为空
    if text == '':
        pass
    
    #接收到数据，打印并回传
    else:
        print(text) 
        s.send(text)
        
    time.sleep(0.1) #100ms查询间隔