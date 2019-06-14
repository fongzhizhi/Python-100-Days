'''
输出1-9999所有的完美数：
完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和，恰好等于它本身。
如果一个数恰好等于它的因子之和，则称该数为“完全数”。第一个完全数是6，第二个完全数是28，第三个完全数是496...
'''
from math import sqrt
import time

start = time.process_time()
sum = 0
for x in range(1,10000):
	#求所有因子之和
	for y in range(1,int(sqrt(x))+1):
		if x%y == 0:
			sum += y
			if y != x/y:
				sum += x/y
	if sum == 2*x:
		print(x)
	sum = 0
end = time.process_time()
print("以上为找到的完美数，用时:", (end - start), "秒")