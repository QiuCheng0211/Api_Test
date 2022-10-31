"""
name_list=["小米","校长","小米1","222","小米333","校长444"]
for name in name_list:
    print(name)

"""
"""
x=y=251 #链式赋值
print(x,y)

a,b,c=1,2,3#系列赋值
print(a,b,c)

a,b=b,a#变量交换
print(a,b,c) #2  1   3
"""

"""
/ 为浮点除法，//整数除法 %取余
print(2**3) #结果为8  **为幂

"""
"""
print(divmod(13,3)) #返回一个数组(4，1)  函数返回当参数 1 除以参数 2 时包含商和余数的元组。
print(round(3.1415926,3))#返回四舍五入的值
"""

"""
import time
a=int(time.time())
print(a)
print(time.time())#获得当前时刻
print(a//60)
"""
"""
import turtle
import  math
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100
turtle.penup()#抬起
turtle.goto(x1,y1)
turtle.pendown()#落下
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.goto(x1,y1)
lem=math.sqrt((x1-x2)**2+(y1-y2)**2)#sqrt开方的意思
turtle.write(lem) #写在图上
print(lem)
"""

"""
a=input("输入一个喜欢的数字")
b="在爱两次"*3
print(a,end="")
print(b)
"""


a='abcdefghijklmnopqrstuvwxyz'  #replace()替换
print(a[1],a[-1])   #[]为索引，正向搜索左侧第一个是0，1 2以此类推，反向的话倒数第一个是-1，-2
print(a.replace("c","沽"))  #调用replace方法 并未改变a变量
print(a)
a=a.replace("c","雨")    #调用replace方法 改变a变量
print(a)

"""
a="to be or not to be"  #split()切割
print(a.split())  #结果['to', 'be', 'or', 'not', 'to', 'be']
print(a.split("be")) #结果['to ', ' or not to ', '']

b=["asx","vjv","dadsa"]
print("".join(b))        #测试join连接 结果为asxvjvdadsa
"""
# python常用序列机构：字符串 列表 元组 字典 集合



