'''
实验名称：土壤湿度传感器
版本：v1.0
日期：2020.3
作者：01Studio 【www.01Studio.org】
说明：通过土壤湿度传感器对土壤湿度测量并在oled显示。
'''

#导入ADC模块
from gpiozero import MCP3004

#导入luma相关库,oled lib
from luma.core.render import canvas
from luma.oled.device import ssd1306

from time import sleep

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3C)

#初始化ADC模块,传感器接到CH1
adc = MCP3004(channel=1)

while True:
    
    V = adc.value*3.3      #采集范围：0-1，转成电压值 0-3.3V

    #土壤湿度：干
    if 0 <= V <= 1.1: 
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Soil_humidity test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' Dry', fill="white")
        print("%.2f"%V + 'V'+' Dry')
         
    #土壤湿度：中 
    if 1.1 < V <= 2.2:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Soil_humidity test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' Normal', fill="white")
        print("%.2f"%V + 'V'+' Normal')
            
    #土壤湿度：湿
    if 2.2 < V <=3.3:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Soil_humidity test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' Wet', fill="white")
        print("%.2f"%V + 'V'+' Wet')
        
    sleep(1) #采集间隔1秒
    