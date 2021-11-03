"""
#输出斐波那契数列
def Fibonacci_Sequence(num): 
    'num = 斐波那契数列的第num项'

    Fibonacci_List = [0,1]
    if num == 0:
        return Fibonacci_List[0]
    elif num == 1:
        return Fibonacci_List
    else:
        for i in range(2,num+1):
            Fibonacci_List.append(Fibonacci_List[i-1] + Fibonacci_List[i-2])
    return Fibonacci_List

num = int(input())                #输入所求项数
print(help(Fibonacci_Sequence))   #打印函数帮助文档
print(Fibonacci_Sequence(num))


#文件的基本操作

file_path = input("请输入文件路径（以enter结束）：")
file_act = 'r'      #默认为只读模式
while(file_act != 'q'):
    file_act = input("请输入所要进行的操作：(可选w,r,a三种模式)，按q退出")   
    if(file_act == 'w') or (file_act == 'a'):
        f = open(file_path,file_act)
        file_str = input("请输入所需要添加的内容（以enter结束）:")
        if(f.write(file_str + '\n') != 0):
            print("写入成功！")
        f.close()
    elif (file_act == 'r'):
        f = open(file_path,file_act)
        str = f.read()
        if(str != 0):
            print("读取成功！")
            print(str)
        f.close()
    elif(file_act == 'q'):
        print("拜拜啦！")
    else:
        print("操作命令错误！")




# 类和对象

# 定义一个父类
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

    def display1(self):
        print(f" name = {self.name}\n sex = {self.sex}\n age = {self.age}\n")


class BasketballPlayer(Person):  # 定义一个篮球运动员的子类
    def __init__(self, height, weight, speed, name, sex, age):     # 重写init
        super().__init__(name, sex, age)
        self.height = height  # 身高
        self.weight = weight  # 体重
        self.speed = speed  # 速度

    def display2(self):
        print(f" height = {self.height}\n weight = {self.weight}\n speed = {self.speed}")


class CarDriver(Person):     # 定义另一个子类
    def display1(self):      # 此处将父类中的方法重写
        print(f"my name is {self.name},i am {self.age} years old\n")


YaoMing = BasketballPlayer(221, 200, 20, "YaoMing", "male", 40)
Father = CarDriver("Yao", "male", 50)
Father.display1()
YaoMing.display1()
YaoMing.display2()

"""
#

# 密码库
# pwd_lib = {'admin': '123456', 'yaoshangshu': '000000', 'hahaha': 'yao1234'}


# 登录按键动作
# def btn_click():
#     value = pwd_lib.get(user_name.text())
#     if value:
#         if value == user_key.text():
#             print("登录成功")
#         else:
#             print("密码错误")
#     else:
#         print("未查找到用户名")
#
#
# if __name__ == "__main__":
#     app = Qt.QApplication(sys.argv)
#     # 创建一个窗口
#     my_win = Qt.QWidget()
#     my_win.setWindowTitle("登录界面")
#     my_win.resize(500, 500)
#     # 添加按钮
#     login_btn = Qt.QPushButton("登录", my_win)
#     # 设置按钮x,y,宽，高   左上角为原点
#     login_btn.setGeometry(200, 350, 100, 50)
#     # 按钮绑定动作
#     login_btn.clicked.connect(btn_click)
#
#     # 添加编辑框
#     user_name = Qt.QLineEdit(my_win)
#     user_name.setGeometry(100, 100, 300, 50)
#     user_key = Qt.QLineEdit(my_win)
#     user_key.setGeometry(100, 200, 300, 50)
#     # 密码用密文显示
#     user_key.setEchoMode(Qt.QLineEdit.Password)
#     # 添加文本框
#     user_name_label = Qt.QLabel("用户名", my_win)
#     user_name_label.setGeometry(100, 80, 60, 20)
#     user_key_label = Qt.QLabel("密码", my_win)
#     user_key_label.setGeometry(100, 180, 60, 20)
#     # 显示窗口
#     my_win.show()
#     # 等待app事件
#     sys.exit(app.exec_())

# 人脸识别基础操作
import cv2
# 开启默认摄像头
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 加载脸部识别的xml文件
face = cv2.CascadeClassifier("D:/python/Setup/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

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
    for(x, y, w, h) in face_list:
        # 画矩形（ 图像 = img  矩形对角点  框的颜色(BGR)  线条厚度 ）
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    # 显示图片
    cv2.imshow("video", img)
    # 按键检测退出
    if (cv2.waitKey(1) & 0xff) == ord('q'):
        break

# 释放摄像头
cap.release()
# 关闭所有OPENCV创建的窗口
cv2.destroyAllWindows()
