import cv2


# 获取人脸信息
def face_get():
    # 先输入userID
    usr_id = input("请输入用户名ID：")
    # 开启默认摄像头
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # 加载脸部识别的xml文件
    face = cv2.CascadeClassifier("D:/python/Setup/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
    # 定义一个计数器
    count = 0
    # 判断摄像头是否开启
    while cap.isOpened():
        # 读取图片信息
        ret, img = cap.read()
        # 把彩色照片转换为灰度图
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 对灰度图片进行检测   所有脸的坐标放入face_list中
        # （灰度图片 = gray_img scaleFactor = 1.1(默认)越大越有可能丢失物体 minNeighbors = 重叠检测，默认为3 minSize =最小像素点）
        face_list = face.detectMultiScale(gray_img,
                                          scaleFactor=1.1,
                                          minNeighbors=5,
                                          minSize=(32, 32))
        # 如果有脸  将脸用矩形框起来
        for (x, y, w, h) in face_list:
            # # 写文字 （图像 = img ,str = 文字 ，坐标，字体，大小，颜色（BGR），粗细）
            # cv2.putText(img, '???', (x + w + 5, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 3)
            cv2.imwrite("D:\\Study_File\\python_study\\Face_Train\\User." + usr_id + '.' + str(count) + ".jpg",
                        gray_img[y:y + h, x:x + w])
            count += 1
            # 画矩形（ 图像 = img  矩形对角点  框的颜色(BGR)  线条厚度 ）
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        if count > 100:
            print("人脸采集完成，摄像头退出...")
            break
        # 显示图片
        cv2.imshow("video", img)
        # 按键检测退出
        if (cv2.waitKey(1) & 0xff) == ord('q'):
            break

    # 释放摄像头
    cap.release()
    # 关闭所有OPENCV创建的窗口
    cv2.destroyAllWindows()
