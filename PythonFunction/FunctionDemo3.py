#收集参数
#在参数前面加*将所有值放置在同一个元组中。
def print_num(*num):
    print(num)
print_num(4)
print_num(1,2,3)
#普通参数和带*号参数一起使用
def print_num2(a,*num):
    print(a)
    print_num(num)
print_num2("num:",1,2,3)
print_num2("num")
#使用**,返回的是字典
def print_num3(**num):
    print(num)
print_num3(x=1,y=2,z=3)

#结合使用
def print_num4(x,y,z=3,*a,**b):
    print(x,y,z)
    print(a)
    print(b)
print_num4(1,2,3,5,6,7,foo=1,bar=2)

#逆收集
def add(x,y):
    print(x+y)
a=(1,2)
add(*a)