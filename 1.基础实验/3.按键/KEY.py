'''
实验名称： 按键
版本： v1.0
日期： 2020.3
作者： 01Studio
社区： www.01studio.org
'''

from gpiozero import Button,LED #导入相关模块

#KEY为IO12,LED为IO4 （BCM编码）
KEY1 = Button(12)
LED_R  = LED(4)

while True:
    
    #判断安静KEY1是否被按下
    if KEY1.is_pressed:
        LED_R.on()
        print("KEY1 is pressed")
        
    else:
        LED_R.off()
        print("KEY1 is not pressed")