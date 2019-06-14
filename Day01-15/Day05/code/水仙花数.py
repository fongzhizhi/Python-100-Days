'''
输出所有的水仙花数：
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），
水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
'''
a = 0 #百位
b = 0 #十位
c = 0 #个位
for x in range(100,1000):
	a = x // 100
	b = x // 10 % 10
	c = x % 10
	if a**3 + b**3 + c**3 == x:
		print(x)
