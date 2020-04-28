'''
实验名称：超声波传感器
版本：v1.0
日期：20120.3
作者：01Studio 【www.01Studio.org】
说明：通过超声波传感器测距，并在OLED上显示。
'''

from gpiozero import DistanceSensor

#导入luma相关库,oled lib
from luma.core.render import canvas
from luma.oled.device import ssd1306

from time import sleep

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3c)

#初始化超声波传感器：echo=15 , trig =14
sensor = DistanceSensor(echo=15, trigger=14)

while True:
    
    #将单位变成cm
    distance = sensor.distance *100
    
    #显示结果保留2位小数
    with canvas(device) as draw:
        draw.text((0, 0),  '01Studio', fill="white")
        draw.text((0, 15), 'Distance test:', fill="white")
        draw.text((0, 35), str("%.2f"%distance)+' CM' , fill="white")

    print('Distance to nearest object is %.2f'%distance, 'CM')
    
    sleep(0.5) #采集间隔