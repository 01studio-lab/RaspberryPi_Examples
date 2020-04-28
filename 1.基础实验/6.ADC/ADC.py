'''
实验名称：ADC-电压测量
版本：v1.0
日期：2020.3
作者：01Studio
说明：通过对ADC数据采集，转化成电压并打印数据
社区：www.01studio.org
'''

#导入相关模块
from gpiozero import MCP3004
from time import sleep

#初始化ADC模块
adc = MCP3004(channel=0)

while True:
    
    V = adc.value*3.3      #采集范围：0-1，转成电压值 0-3.3V
    print("%.2f"%V + ' V') #保留2位小数
    sleep(1)
    