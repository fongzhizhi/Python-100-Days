'''
输入收入和五险一金计算个人所得税:
假设月征税标准如下：
[0,3000]		3%		0
(3000,12000]	10%		210
(12000,25000]	20%		1410
(25000,35000]	25%		2660
(35000,55000]	30%		4410
(55000,80000]	35%		7160
(80000,~]		45%		15160
'''
salary  = float(input('本月收入: '))
insurance = float(input('五险一金等应扣额: '))
diff = salary  - insurance - 3500 #起征3500

rate = 0 #税率
deNum = 0 #速算扣除数

if diff <= 3000:
	rate = 0.03
	deNum = 0
elif diff <= 12000:
	rate = 0.1
	deNum = 210
elif diff <= 25000:
	rate = .2
	deNum = 1410
elif diff <= 35000:
	rate = .25
	deNum = 2660
elif diff <= 55000:
	rate = .3
	deNum = 4410
elif diff <= 80000:
	rate = .35
	deNum = 7160
else:
	rate = .45
	deNum = 15160

tax = abs(diff * rate - deNum) #个人所得税
sal = diff + 3500 - tax

print('税前工资%.2f,扣除五险一金,个人所得税为：%.2f,实际到手工资：%.2f' % (salary, tax, sal))