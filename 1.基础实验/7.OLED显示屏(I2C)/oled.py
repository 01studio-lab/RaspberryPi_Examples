'''
实验名称：OLED显示屏（I2C总线）
版本：v1.0
日期：2020.3
作者：01Studio
参考链接: https://luma-oled.readthedocs.io/en/latest/python-usage.html
'''
#导入luma相关库
from luma.core.render import canvas
from luma.oled.device import ssd1306

#初始化oled，I2C接口1,oled地址是0x3c
device = ssd1306(port=1, address=0x3C)

#显示字符，with...as...使用好处是可以自动处理异常
with canvas(device) as draw:
    draw.text((0, 0),  'Hello World!', fill="white")
    draw.text((0, 20), 'Raspberry Pi', fill="white")
    draw.text((0, 50), 'By 01Studio', fill="white")