'''
计算两个数的最大公约数和最小公倍数
'''
a = int(input('请输入一个数字:'))
b = int(input('请输入第二个数字:'))
if a>b:
	c = b
	b = a
	a = c
maxdivisor = 1
for x in range(a,0,-1):
	if a%x == 0 and b%x == 0:
		maxdivisor = x
		break
product = a * b / maxdivisor
print('%d和%d的最大公约数为%d，最小公倍数为%d' % (a,b,maxdivisor,product))