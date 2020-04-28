'''
实验名称：录制视频
版本： v1.0
日期： 2020.3
作者： 01Studio
说明：通过编程实现摄像头模块录制视频
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


#录制视频，10秒
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(10)
camera.stop_recording()

#关闭摄像头
camera.stop_preview()