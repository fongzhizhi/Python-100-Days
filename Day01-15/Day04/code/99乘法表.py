'''
输出九九乘法表
1*1
2*1 2*2
3*1 3*2 3*3
'''
i = 1
s = ''
for x in range(1,10): #9行
	while i <= x: # x列
		pro = x * i
		s += '%d*%d=%d\t' % (x,i,pro)
		i += 1
	print(s)
'''
+ 字符串拼接时由于数据类型差异会报错，比如2+'s'，数字2不会像某些语言那样转为字符串再拼接。
+ 这里print()默认的结束符是回车符，其实可以自定义结束符，比如以tab键符号结束，就可以这样写：
	print('%d*%d=%d' % (x,i,pro), end='\t')
'''