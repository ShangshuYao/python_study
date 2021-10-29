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

"""


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
