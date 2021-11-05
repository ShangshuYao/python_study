import os
from PIL import Image
import numpy
import cv2

# 创建一个训练器
train_recognizer = cv2.face.LBPHFaceRecognizer_create()


# 训练识别器
def face_train():
    # 载入人脸识别xml文件
    face = cv2.CascadeClassifier("D:/python/Setup/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    # 照片所在的文件夹
    img_path = 'D:\\Study_File\\python_study\\Face_Train'
    # 获取文件夹里面所有的文件名并写入列表   列表推导
    all_img_paths = [os.path.join(img_path, img) for img in os.listdir(img_path)]
    ids_list = []
    faces_list = []
    for each_img in all_img_paths:
        ids = int(os.path.split(each_img)[-1].split('.')[1])
        PIL_img = Image.open(each_img).convert("L")
        np_img = numpy.array(PIL_img, 'uint8')
        face_sample = face.detectMultiScale(np_img)
        for (x, y, w, h) in face_sample:
            faces_list.append(np_img[y:y + h, x:x + w])
            ids_list.append(ids)
    print("开始训练...")
    train_recognizer.train(faces_list, numpy.array(ids_list))
    print("训练完成，生成yml文件")
    train_recognizer.write("people.yml")


# 进行识别
def face_recognition():
    name = []
    # 加载文件
    train_recognizer.read("people.yml")
    # 开启默认摄像头
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 加载脸部识别的xml文件
    face = cv2.CascadeClassifier("D:/python/Setup/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    print("人脸识别中...\n按‘q’退出")
    # 判断摄像头是否开启
    while camera.isOpened():
        # 读取图片信息
        ret, img = camera.read()
        # 把彩色照片转换为灰度图
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 对灰度图片进行检测   所有脸的坐标放入face_list中
        # （灰度图片 = gray_img scaleFactor = 1.1(默认)越大越有可能丢失物体 minNeighbors = 重叠检测，默认为3 minSize =最小像素点）
        face_list = face.detectMultiScale(gray_img,
                                          scaleFactor=1.1,
                                          minNeighbors=3,
                                          minSize=(32, 32))
        # 如果有脸  将脸用矩形框起来
        for(x, y, w, h) in face_list:
            ids, pre = train_recognizer.predict(gray_img[y:y+h, x:x+w])
            if ids == 1001:
                name = "Yao"
            elif ids == 1002:
                name = "Bryant"
            # 写文字 （图像 = img ,str = 文字 ，坐标，字体，大小，颜色（BGR），粗细）
            cv2.putText(img, name, (x+w+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)
            # 画矩形（ 图像 = img  矩形对角点  框的颜色(BGR)  线条厚度 ）
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 显示图片
        cv2.imshow("video", img)
        # 按键检测退出
        if (cv2.waitKey(1) & 0xff) == ord('q'):
            break

    # 释放摄像头
    camera.release()
    # 关闭所有OPENCV创建的窗口
    cv2.destroyAllWindows()
