# coding=utf-8
from msg import *

'''
# 这个因为到包,所以__all__不起作用
from snbc import *
print(snbc.add(1, 2))
print(snbc.addd(1, 2))
'''

'''
# 因为到包了,所以__all__起作用了
from snbc.snbc import *
print(add(1, 2))
print(addd(1, 2))
'''

# if __name__ == '__main__':
result = test.add(1, 2)
print(result)
result = test.addd(1, 2)
print(result)

# 编辑的时候就错误,因为没有导入
# test2.
