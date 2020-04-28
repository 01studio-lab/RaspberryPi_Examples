'''
实验名称：系统信息显示
版本： v1.0
日期： 2020.3
作者： 01Studio
说明：通过编程采集树苺派系统信息，并在oled显示。
社区：www.01studio.org
'''

#导入相关库
import os

#IP lib
import socket, fcntl, struct

#oled lib
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep

#oled 初始化
device = ssd1306(port=1, address=0x3c)

#采集CPU温度信息，返回字符                                     
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

#返回CPU使用率百分比（%），字符类型                             
def getCPUuse():
    return(str(os.popen("top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))

# 采集RAM信息，返回单位是kB                                      
# Index 0: 总内存                                                               
# Index 1: 已使用内存                                                               
# Index 2: 剩余内存                                                               
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])
 
# 返回SD卡容量大小，单位是GB                    
# Index 0: 总容量                                                        
# Index 1: 已用空间                                                        
# Index 2: 剩余空间                                                    
# Index 3: 使用率（%）                                                 
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

#获取本地IP地址，返回字符
def getIP(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    #异常处理
    try:
        return socket.inet_ntoa(fcntl.ioctl( 
            s.fileno(), 
            0x8915,  # SIOCGIFADDR 
            struct.pack('256s', ifname[:15].encode('utf-8')) 
           )[20:24])
    
    except OSError:
        return('0.0.0.0')

while True:
     
    #采集CPU温度信息
    CPU_temp = getCPUtemperature()
    
    #采集CPU使用率
    CPU_usage = getCPUuse()
     
    #内存信息，转化成MB
    RAM_stats = getRAMinfo()
    RAM_total = int(int(RAM_stats[0]) / 1000)
    RAM_used = int(int(RAM_stats[1]) / 1000)
    RAM_free = int(int(RAM_stats[2]) / 1000)
    RAM_perc = str(round((RAM_used/RAM_total*100),1))+'%'
     
    #sd卡容量信息
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3] #使用百分比
    
    #本地IP信息，可通过在终端运行ifconfig指令查看网卡名称
    IP=getIP("wlan0") 

    #oled显示
    with canvas(device) as draw:
        
        draw.text((0, 0),  'CPU Temp: ' + CPU_temp + ' C', fill="white")
        draw.text((0, 10), 'CPU Used: ' + CPU_usage + ' %', fill="white")
        draw.text((0, 24), 'RAM:' + str(RAM_used) + '/' + str(RAM_total)+' MB' + ' '+RAM_perc, fill="white")
        draw.text((0, 38), 'DISK:' + str(DISK_used) + '/' + str(DISK_total) +' '+ DISK_perc, fill="white")
        draw.text((0, 52), 'IP:'+ IP, fill="white")

    sleep(0.5) #延时，数据更新间隔