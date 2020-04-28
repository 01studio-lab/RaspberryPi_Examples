'''
实验名称：水位传感器
版本：v1.0
日期：2020.3
作者：01Studio 【www.01Studio.org】
说明：通过水位传感器测量水位（液位）高度并在oled显示。
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

    #水位：0-1cm
    if 0 <= V <= 0.48: 
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Water_level test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' 0-1cm', fill="white")
        print("%.2f"%V + 'V'+' 0-1cm')
         
    #水位：1-2cm
    if 0.48 < V <= 0.73:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Water_level test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' 1-2cm', fill="white")
        print("%.2f"%V + 'V'+' 1-2cm')
            
    #水位：2-3cm
    if 0.73 < V <=0.97:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Water_level test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' 2-3cm', fill="white")
        print("%.2f"%V + 'V'+' 2-3cm')

    #水位：3-4cm
    if 0.97 < V <=1.05:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Water_level test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' 3-4cm', fill="white")
        print("%.2f"%V + 'V'+' 3-4cm')
        
    #水位：>4cm
    if 1.05 < V :
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'Water_level test:', fill="white")
            draw.text((0, 40), str("%.2f"%V) + 'V'+' >4cm', fill="white")
        print("%.2f"%V + 'V'+' >4cm')
        
    sleep(1) #采集间隔1秒
    