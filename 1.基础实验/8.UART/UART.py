'''
实验名称：串口通信
版本： v1.0
日期： 2020.3
作者： 01Studio
说明：通过编程实现串口通信，跟电脑串口助手实现数据收发。
社区：www.01studio.org
'''

import serial
import time

# 配置串口
com = serial.Serial("/dev/ttyS0", 115200)

#发送提示字符
com.write(b'Hello 01Studio!')

while True:
    
    # 获得接收缓冲区字符个数 int
    count = com.inWaiting()
    
    if count != 0:
        # 读取内容并打印
        recv = com.read(count)
        print(recv)
        
        #发回数据
        com.write(recv)
        
        # 清空接收缓冲区
        com.flushInput()
        
    # 延时100ms,接收间隔
    time.sleep(0.1)