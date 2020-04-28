'''
实验名称：水位传感器
版本：v1.0
日期：2020.3
作者：01Studio 【www.01Studio.org】
说明：通过水位传感器测量水位（液位）高度并在oled显示。
'''

#bmp280 lib
import bmp280

#导入luma相关库,oled lib
from luma.core.render import canvas
from luma.oled.device import ssd1306

import time

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3c)

#构建BMP280对象，I2C接口1
b = bmp280.BMP280(port=1)

while True:
    
    #获取温度
    Temp  = b.getTemp()
    
    #获取大气压强
    Pressure = b.getPressure()
    
    #获取海拔高度
    Altitude = b.getAltitude()
    
    with canvas(device) as draw:
        draw.text((0, 0),  '01Studio', fill="white")
        draw.text((0, 15), 'BMP280 test:', fill="white")
        draw.text((0, 35), str("%.2f"%Temp)+' C' , fill="white")
        draw.text((0, 45), str("%.2f"%Pressure)+' Pa' , fill="white")
        draw.text((0, 55), Altitude +' M', fill="white")
        
    #print values
    print("Temperature in Celsius : %.2f C" %Temp)
    print("Pressure : %.2f hPa " %Pressure)
    print('Altitude : ' + Altitude+' M')
    
    #sleep of 1s
    time.sleep(1)
