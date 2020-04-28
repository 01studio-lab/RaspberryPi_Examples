'''
实验名称：人体感应传感器
版本：v1.0
日期：2020.3
作者：01Studio
社区：www.01studio.org
'''

from gpiozero import MotionSensor, LED
from signal import pause

#构建对象
People = MotionSensor(18)
LED_R = LED(4)

def fun1():
    LED_R.on()
    print('Got People!!!')
    
def fun2():
    LED_R.off()
    print('No People!!!')

#定义动作执行，有人时候点亮LED
People.when_motion = fun1
People.when_no_motion = fun2

#阻塞IO,让程序持续运行
while True:
    pass