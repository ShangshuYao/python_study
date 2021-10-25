import os

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

os.system("pause")


