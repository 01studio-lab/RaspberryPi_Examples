'''
实验名称：外部中断
版本：v1.0
日期：2020.3
作者：01Studio
社区：www.01studio.org
'''

from gpiozero import Button,LED

KEY1 = Button(12)
LED_R=LED(4)

def fun():
    
    LED_R.toggle() #LED红灯状态翻转

#设置按键中断
KEY1.when_pressed = fun

#阻塞线程，让程序持续执行
while True:
    pass