#如果使用可变的数据结构(列表)当作参数，情况会有所不同
def change(n):
    n[0]=[1]
a=[2,3]
change(a)
print(a)
#这个时候原来的数据结构会发生变化，再传入参数时需要传入这个参数的副本
b=[2,3]
c=b[:]
change(c)
print(b)
print(c)

#使用函数初始化一个字典,可以使用这套函数实现人名的查找
#初始化总字典
def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}

storage={}
init(storage)
print(storage)
#获得名字的函数
def lookup(data,lable,name):
    return data[lable].get(name)

#存储名字的函数
def store(data,full_name):
    names=full_name.split()
    if len(names)==2:
        names.insert(1,'')
    lables='first','middle','last'
    for lable,name in zip(lables,names):
        people=lookup(data,lable,name)
        if people:
            people.append(full_name)
        else:
            data[lable][name]=[full_name]

MyNames={}
init(MyNames)
store(MyNames,"Magnus Lie Hetland")
lookup(MyNames,'middle','Lie')
print(lookup(MyNames,'middle','Lie'))

