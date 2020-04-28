'''
实验名称：MQTT通信
版本：v1.0
日期：2020.3
作者：01Studio
说明：编程实现MQTT通信:发布者（publish）。
'''

import paho.mqtt.client as mqtt
import time

#服务器和主题信息
host = 'mqtt.p2hp.com'
port = 1883
topic = '/public/01Studio/1'

#构建mqtt客户端对象
client = mqtt.Client()

#发起连接
client.connect(host,port)

while True:
    
    #发布信息
    client.publish(topic,'Hello 01Studio!')
    
    time.sleep(1) #延时1秒，发送间隔
