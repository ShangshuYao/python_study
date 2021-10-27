import os
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

"""
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
os.system("pause")


