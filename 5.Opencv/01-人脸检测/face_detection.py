'''
实验名称：Opencv人脸检测
版本： v1.0
日期： 2020.9
作者： 01Studio
说明：使用openmv库对图片进行人脸检测
社区：www.01studio.org
Openmv库简易安装教程：https://www.jb51.net/article/171599.htm/
'''

import cv2
image=cv2.imread("faces.jpg") #要识别的图片
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(5,5))
print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("dect",image) #缓冲显示
cv2.imwrite("result.jpg",image) #保存结果

cv2.waitKey(0)
cv2.destroyAllWindows()
