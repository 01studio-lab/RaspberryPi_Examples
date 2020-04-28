'''
实验名称：摄像头模块
版本：v1.0
日期：2020.3
作者：01Studio
说明：使用摄像头模块拍照并保存
社区：www.01studio.org
'''

#导入相关库
from picamera import PiCamera
from time import sleep

#构建摄像头
camera = PiCamera()

#打开摄像头
camera.start_preview()

sleep(3) #等待摄像头稳定

#拍摄照片5张并保存到桌面
for i in range(5):
    camera.capture('/home/pi/Desktop/'+str(i)+'.jpg')

#关闭摄像头
camera.stop_preview()