'''
实验名称:有源蜂鸣器
版本：v1.0
日期：2023.3
作者：01Studio
说明：让有源蜂鸣器发出滴滴响声
社区：www.01studio.org
'''

from gpiozero import Buzzer
import time

#引脚16,底电平发出响声
beep = Buzzer(16,active_high=False)

while True:
    
    #循环发出响声
    beep.on() 
    time.sleep(1)
    beep.off()
    time.sleep(1)
    