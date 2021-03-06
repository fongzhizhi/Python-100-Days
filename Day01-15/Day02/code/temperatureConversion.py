'''
温度转换：
摄氏温度c ,将其转化为华氏温度f ,转换公式为：f=1.8*c+32.
'''
print('您将要输入的是否为摄氏温度，是则输入', '1', '或', 'y', '否则输出其他字符:')
isC = input()
isC = isC == '1' or isC == 'y'
a = 32.00
c = 0.0

if isC:
	print('请输出摄氏温度:')
	c = float(input())
	f = 1.8 * c + 32
	print('%.2f摄氏度转为华氏温度为:%.2f' % (c, f))
else:
	print('请输入华氏温度:')
	f = float(input())
	c = (f - 32) / 1.8
	print('%.2f华氏温度转为摄氏度为:%.2f' % (f, c))

'''
总结：
+ print() 可在命令行输出字符串，input() 获取屏幕输入的字符串
+ 在Python中判断是否相等的运算符为==，不支持 ===
+ Python中的逻辑运算符为 not or and，不支持 ! || && 这种常见的表示
+ float() 将数据转为字符类型
+ print() 函数支持格式化的字符串，采用和C语言一样的运算符 % 
'''
