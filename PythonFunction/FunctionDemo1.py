#函数
#函数分为俩种，系统自带的函数和自定义函数
#系统自带的函数可以直接使用，但是灵活性较低
#部分系统自带的函数
a="asd"
print(len(a))

b="asduasd"
print(b.split('u'))

#自定义的函数
def a():
   print("Chall")
a()

#创建斐波那契函数
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result
print(fibs(10))

#文档化函数
#用来给对函数的功能进行描述
#使用函数名.__doc__或者help(函数名)进行调用
def add(a,b):
    """这是一个用来进行加法的函数"""
    c=a+b;
    return c
print(add.__doc__)
print(help(add))

#python中的return也起到结束函数的作用,return后面的语句不会执行
def stop():
    print(3)
    return
    print(2)
stop()
#x=stop()
#print(x)