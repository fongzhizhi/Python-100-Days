'''
掷骰子决定做什么
'''
import random

num = random.randint(1, 6)

if num == 1:
	print('singing')
elif num == 2:
	print('dancing')
elif num == 3:
	print('reading')
elif num == 4:
	print('again')
elif num == 5:
	print('nothing')
else:
	print('anthing')

'''
+ random 模块的randint(a, b)方法可以返回[a,b]之间的随机整数
'''
