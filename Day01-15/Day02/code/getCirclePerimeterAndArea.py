'''
根据输入的半径计算圆的周长和面积
'''
import math
r = float( input('请输入圆的半径:') )

perimeter = 2 * math.pi * r
area = math.pi * r ** 2

print('半径为%.2f的圆的周长为：%.2f,面积为：%.2f' % (r, perimeter, area))

'''
总结：
+ 使用到的圆周率π为常量，为内部模块math的属性，需要使用math需要使用 import 关键字进行导入
+ 指数运算符为 ** 而不是 ^ (此为按位异或)。
'''