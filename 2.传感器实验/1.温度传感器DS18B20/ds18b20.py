'''
实验名称：温度传感器DS18B20
版本：v1.0
日期：2020.3
作者：01Studio
说明：通过编程采集温度数据，并在oled显示。
'''
#Sensor lib
from w1thermsensor import W1ThermSensor

#导入luma相关库,oled lib
from luma.core.render import canvas
from luma.oled.device import ssd1306

from time import sleep

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3C)

#################DS18B20对象构建###################################
#构建方法1：需要知道传感器地址
#DS18B20 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "000005e35af8")

#构建方法2：无需知道传感器地址，只有1个传感器连接时适用
DS18B20=W1ThermSensor()

while True:

    temperature = DS18B20.get_temperature() #数据采集
    
    #oled显示温度信息,结果保留2位小数
    with canvas(device) as draw:
        draw.text((0, 0),  '01Studio', fill="white")
        draw.text((0, 15), 'Temp test:', fill="white")
        draw.text((0, 40), '%.2f'%temperature+' C', fill="white")
    
    print('%.2f'%temperature) #打印显示
    
    sleep(2) #采集间隔2秒