'''
输出n位以内的斐波那契数列：
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）
以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用，为此，
美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。
'''
n = abs(int(input('你想获得多少位斐波那契数列：')))
if n < 3:
	for i in range(1,n+1):
		print(1, end='、')
else:
	print('1、1', end='、')
	F2 = 1
	F1 = 1
	for j in range(3,n+1):
		Fj = F1 + F2
		F2 = F1
		F1 = Fj
		print(Fj, end='、')