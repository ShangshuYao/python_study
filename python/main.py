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

def FileControl(path,str):

    """
    输入： path = 所要打开的文件路径   str = 向文件中添加的字符串
    输出： 无
    返回值： true--成功   -1 --失败 
    """

    file = open(path,'a')   #新建一个文件用于追加，文件指针放在文件末尾
    if file == False:      
        return -1
    else:       
        file.write(str)   #向文件中写入字符串
        file.close()        #关闭文件


file_path = input("请输入文件路径（以enter结束）：")
file_str = input("请输入所需要添加的内容（以enter结束）:")
FileControl(file_path,file_str)
f = open(file_path)
str = f.read()
f.close()
print(FileControl.__doc__)
print(str)

os.system("pause")


