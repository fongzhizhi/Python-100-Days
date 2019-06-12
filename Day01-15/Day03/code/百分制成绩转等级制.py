'''
百分制成绩转等级制
[0,60) --- E
[60,70) --- D
[70,80) --- C
[80,90) --- B
[90,100] --- A
'''
score = float(input('请输入你的分值：'))
index = (score - 60) / 10
level = 'E'

if index < 0:
	level = 'E'
elif index < 1:
	level = 'D'
elif index < 2:
	level = 'C'
elif index < 3:
	level = 'B'
else:
	level = 'A'

print('你的分值级别为：', level)
