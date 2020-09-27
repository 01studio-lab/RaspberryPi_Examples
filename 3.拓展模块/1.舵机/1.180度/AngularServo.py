'''
实验名称：180度舵机
版本：v1.0
日期：2020.3
作者：01Studio
说明：通过编程让舵机转至不同角度。
'''

from gpiozero import AngularServo
from time import sleep

#构建舵机对象 SG90 180' Servo
servo = AngularServo(20, min_angle=-90, max_angle=90,min_pulse_width=0.0005, max_pulse_width=0.0025)

while True:
    
    #转至不同角度
    servo.angle = -90
    sleep(1)
    
    servo.angle = -45
    sleep(1)
    
    servo.angle = 0
    sleep(1)
    
    servo.angle = 45
    sleep(1)
    
    servo.angle = 90
    sleep(1)