'''
实验名称：180度舵机（树梅派防抖动版）
版本：v1.0
日期：2020.9
作者：01Studio
说明：通过编程让舵机转至不同角度。
     先安装pigpio库，终端输入下面指令：
     sudo apt-get install python3-pigpio
     sudo pigpiod
'''

#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time

servo = 20

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency( servo, 50 )
while True:
    print( "0 deg" )
    pwm.set_servo_pulsewidth( servo, 500 ) ;
    time.sleep( 1)

    print( "90 deg" )
    pwm.set_servo_pulsewidth( servo, 1500 ) ;
    time.sleep( 1 )

    print( "180 deg" )
    pwm.set_servo_pulsewidth( servo, 2500 ) ;
    time.sleep( 1 )

#turning off servo
#pwm.set_PWM_dutycycle(servo, 0)
#pwm.set_PWM_frequency( servo, 0 )
