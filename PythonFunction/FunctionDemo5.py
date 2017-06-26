#使用global关键字在作用域中调用全局变量
x=1
def change_global():
    global x
    x=x+1
change_global()
print(x)

#嵌套的作用域(闭包)
def multipler(factory):
    def multiplerByFactor(number):
        return number*factory
    return multiplerByFactor

double=multipler(2)
print(double(5))
triple = multipler(3)
print(triple(3))
print(multipler(5)(4))
#python3中引入nonlocal关键字，用于获取外部作用域中的变量

#俩个经典的递归
#求n的阶乘
def factorial(n):
    if n==1:
        return n;
    else:
        return n*factorial(n-1)
#求幂
def power(x,n):
    if n==0:
        return 1
    else:
        return x*power(x,n-1)