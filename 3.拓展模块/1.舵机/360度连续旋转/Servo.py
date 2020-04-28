'''
实验名称：360度连续旋转舵机
版本：v1.0
日期：2020.3
作者：01Studio
说明：通过编程让连续旋转舵机以不同速度转动。
'''

from gpiozero import Servo
from time import sleep

#SG90 360' Servo
servo = Servo(20)

while True:

    #以不同速度旋转
    servo.value = -1.0
    sleep(2)
    
    servo.value = -0.5
    sleep(2)
    
    servo.value = None #停止
    sleep(2)
    
    servo.value = 0.5
    sleep(2)
    
    servo.value = 1.0
    sleep(2)