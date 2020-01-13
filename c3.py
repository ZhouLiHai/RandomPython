
# 创建字典的方式

a = dict(one=1,two=2,three=3)
b = {'one':1, 'two':2,'three':3}
c = dict(zip(['one', 'two', 'three'],[1, 2, 3]))
d = dict([('one',1),('two',2),('three',3)])
print(a == b == c == d)

# 字典推导
a = [('one',1),('two',2),('three',3)]
reversed_dict = {n : name for name, n in a}
print(reversed_dict)

# dict.get(k, default)方法并不是处理找不到键的好方法
index = {}
index.setdefault('a', []).append(1)
#这样写，只需要一次查询操作。
index.setdefault('a', []).append(2)
print(index)

# 有时defaultdict方式更有效,永远不会找不到键
import collections

index = collections.defaultdict(list)
index['a'].append(1)
index['a'].append(2)

print(index)

# __missing__方法
# dict本身没有实现这个方法，但它知道这个方法的存在
# 如果有一个类继承了dict，并且提供__missing__方法，在找不到键的时候
# 这个方法就会被调用

# 字典变种

a = collections.OrderedDict()

# 容纳数个不同的映射对象，然后一级一级的查找键
b = collections.ChainMap()

# 计数器每次更新键都会增加
ct = collections.Counter('afaefaeaeveafeaefaf')
print(ct)

# 获取一个只读映射
from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy[1])

# 你不能这么做 d_proxy[1] = 'B'

# 集合
# 集合中的元素必须是可散列的,且唯一
l = ['spam','spam','eggs','spam']
print(set(l))

from random import randint

a = [randint(0,10) for _ in range(5)]
b = range(10)

print(a)
print(b)
found = len(set(a) & set(b))
print(found)

# 交、差、并、补
# s & z 
# s | z
# s - z
# s ^ z