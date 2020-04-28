'''
实验名称：流水灯
版本：v2.0
日期：2020.3
作者：01Studio
'''

from gpiozero import LED #导入LED模块
from time import sleep   #导入延时模块

#LED初始化
LED_R= LED(4)
LED_Y= LED(5)
LED_G= LED(6)

#定义数组方便循环语句调用
LED=[LED_R, LED_Y, LED_G]

while True: #while True表示一直循环

    for i in range(0,3): #循环3次

        LED[i].on() #点亮LED
        sleep(1)
        LED[i].off() #关闭LED
