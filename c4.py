# Python3中bytes或者bytearry对象的各个元素都是0～255之间的字符，切片、长度始终是二进制序列的长度。

name = bytes('立海', encoding='utf-8')
print(name)
print(name[:1])

# memoryview与struct配合处理格式化数据

import struct

fmt = '<3s3sHH'

with open('README.md', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
res = struct.unpack(fmt, header)
print(res)

# memoryview 对象的切片是一个新的memoryview对象，而且不会复制字节序列
del header
del img

# 处理编码和解码问题

city = '烟台'
print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))

# 处理文本文件的最佳方式
# 尽早把字节序列解码为字符串，尽量晚的把字符串编码成字节序列
# 程序中只处理str类型

# open使用制定解码器解码
open('README.md', 'w', encoding='utf-8')

