'''
输入年分，判断是平年还是闰年
'''
year = int(input('请输入年份：'))
isNormal = year % 100 != 0 #判断是普通年还是世纪年
isLeap = False

if isNormal:
	isLeap = year % 4 == 0
else:
	isLeap = year % 400 == 0
if isLeap:
	print('%d年是闰年' % year)
else:
	print('%d年是平年' % year)