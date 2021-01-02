import functools

n = [3,5,6,7,8,9]


print(functools.reduce(lambda x,y: x*y,n))

print (functools.reduce(lambda a,b : a+b,n))
