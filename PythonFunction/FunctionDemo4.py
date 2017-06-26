#联系参数的使用
def story(**kwds):
    return 'Once upon a time. there was a %(job)s called %(name)s.' % kwds
def power(x,y,*others):
    if others:
        print("Received redundant parameters:'",others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    'Imitates range() for step > 0'
    if stop is None:
        start,stop=0,start
    result=[]
    i=start
    while i < stop:
        result.append(i)
        i+=step
    return result

print(story(job="king",name="CY"))
print(story(name="CY",job="king"))
params={'job':'language','name':'Python'}
print(story(**params))
del params['job']
print(story(job='asd',**params))
print(power(2,3))
print(power(3,2))
print(power(y=3,x=2))
params2=(5,)*2
print(power(*params2))
print(power(3,3,'casd'))
print(interval(10))
print(interval(1,5))
print(interval(3,12,4))
print(interval(3,7))
print(power(*interval(3,7)))