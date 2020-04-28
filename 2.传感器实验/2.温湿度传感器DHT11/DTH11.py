'''
实验名称：温湿度传感器DHT11
版本：v1.0
日期：2020.3
作者：01Studio
说明：通过编程采集温度数据，并在OLED显示。
社区：www.01studio.org
'''

import Adafruit_DHT,time

#导入luma相关库,oled lib
from luma.core.render import canvas
from luma.oled.device import ssd1306

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3C)

#设置传感器类型: 支持DHT11,DHT22和AM2302
sensor=Adafruit_DHT.DHT11
  
#设置GPIO
gpio=19

while True:    

    #读取传感器数据,读取失败会重复15次，间隔2秒
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    
    # 为了避免偶尔读取失败，先判断是否读取成功，再打印相关数据
    if humidity is not None and temperature is not None:
            #oled显示温度信息,结果保留2位小数
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'DHT11 test:', fill="white")
            draw.text((0, 40), '%.1f'%temperature+' C'+'  '+'%.1f'%humidity+' %', fill="white")
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))

    else:
        with canvas(device) as draw:
            draw.text((0, 0),  '01Studio', fill="white")
            draw.text((0, 15), 'DHT11 test:', fill="white")
            draw.text((0, 40), 'Failed to read!', fill="white")
        
        print('Failed to get reading. Try again!')
        
    
    time.sleep(2)
