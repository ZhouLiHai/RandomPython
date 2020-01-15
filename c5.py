def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)    
print(factorial(12))

print(factorial.__doc__)
print(type(factorial))

fact = factorial

print(fact(12))

# 高阶函数，返回函数的函数
l = ['jfis','apple','cherry','raspberry','banana']

print(sorted(l, key=len))

def reverse(word):
    return word[::-1]

print(sorted(l, key= reverse))

# map reduce

print(list(map(fact, range(6))))
# 生成表达式更加直观
print([fact(n) for n in range(6)])

print(list(map(fact, filter(lambda n: n%2, range(6)))))
# 生成表达式同样更加直观
print([fact(n) for n in range(6) if n%2])

from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))

# 函数内省
print(dir(factorial))
class C: pass
obj = C()
def func(): pass

print(sorted(set(dir(func)) - set(dir(obj))))

print(func.__code__)