'''
判断是不是质素。
	所谓质数或称素数,就是一个正整数,除了本身和 1 以外并没有任何其他因子
'''
from math import sqrt
num = int(input('请输入你要判断的数字:'))
end = int(sqrt(num)) #此处理极大缩短了循环次数
i = 2
flag = True
while  i < end+1:
	if num % i == 0:
		flag = False
		break
	i += 1
print(flag)

'''
+ from math import sqrt即可单独导入sqrt函数
'''