'''
实验名称：流水灯
版本：v1.0
日期：2020.3
作者：01Studio
'''

from gpiozero import LED #导入LED模块
from time import sleep   #导入延时模块

#LED初始化
LED_R= LED(4)
LED_Y= LED(5)
LED_G= LED(6)

while True: #while True表示一直循环
    
    #打开LED，延时1秒后关闭
    LED_R.on()
    sleep(1) #延时1秒
    LED_R.off()
    
    LED_Y.on()
    sleep(1)
    LED_Y.off()
    
    LED_G.on()
    sleep(1)
    LED_G.off()
    