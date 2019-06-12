'''
输入三条边长如果能构成三角形就计算周长和面积
(能构成三角形的三边条件：任意两边之和大于第三边)
'''
import math
a = float(input('请输入第1条边长：'))
b = float(input('请输入第2条边长：'))
c = float(input('请输入第3条边长：'))

if a+b>c and a+c>b and b+c>a:
	l = a+b+c
	p = (a + b + c) / 2
	S = math.sqrt(p * (p - a)*(p - b)*(p - c)) 
	print('构成的三角形周长为%f,面积为%f' % (l, S))
else:
	print('输入的三条边无法构成三角形')