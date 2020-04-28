'''
实验名称：点亮LED
版本：v1.0
日期：2019.9
作者：01Studio
实验目的：学习led点亮。
'''
from gpiozero import LED #从gpiozero库导入LED模块

LED_R= LED(4) #红灯初始化，连接的是树莓派引脚4（BCM编码）

LED_R.on()   #点亮红灯

#阻塞线程，让程序持续执行
while True:
    pass