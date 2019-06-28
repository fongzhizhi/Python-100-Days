from abc import ABCMeta, abstractmethod
import random

class Fighter(object, metaclass=ABCMeta):
	'''Fighter：战斗人员
		:param name:姓名
		:param hp:血量
	'''
	__slots__ = ('_name', '_hp')

	def __init__(self, name, hp):
		self._name = name
		self._hp = hp

	@property
	def name(self):
		return self._name

	@property
	def hp(self):
		return self._hp

	@property
	def is_alive(self):
		return self._hp > 0

	@hp.setter
	def hp(self, hp):
		self._hp = hp

	@abstractmethod
	def attack(self, target):
		pass

	def fixedhp(self, indexhp=0):
		#修正血量，为负时改为0
		self._hp += indexhp
		self._hp = self._hp >= 0 and self._hp or 0

class Ultraman(Fighter):
	"""Ultraman-凹凸曼
		:param pw:战力值
		:param mp:魔法值
	"""
	def __init__(self, name, hp, pw ,mp):
		super().__init__(name, hp)
		self._pw = pw
		self._mp = mp
	
	@property
	def mp(self):
		return self._mp

	@mp.setter
	def mp(self, mp):
		self._mp = mp

	def normal_attack(self, target):
		#普通攻击：不消耗魔法，随机打出战力值5%-10%的攻击力
		propertion = random.randint(5, 10) / 100
		attack_power = self._pw * propertion
		target.fixedhp(-attack_power)

	def magic_attack(self, target):
		#魔法攻击：随机打出战力值20%-40%的魔发伤害，同时消耗100魔法值(魔法值不足时攻击失效)
		if self._mp < 100:
			return False
		propertion = random.randint(20, 40) / 100
		attack_power = self._pw * propertion
		target.fixedhp(-attack_power)
		return True

	def attack(self, target):
		#随机攻击
		if random.randint(0, 1) == 0:
			self.normal_attack(target)
		else:
			self.magic_attack(target)

	def status(self):
		#当前状态
		return '%s当前的血量为%.2f，魔法值为%.2f' % (self._name, self._hp, self._mp)

class Monster(Fighter):
	"""Monster-小怪兽
		:param pw:战力值
	"""
	def __init__(self, name, hp, pw):
		super().__init__(name, hp)
		self._pw = pw
	
	@property
	def mp(self):
		return self._mp

	@mp.setter
	def mp(self, mp):
		self._mp = mp

	def attack(self, target):
		#普通攻击：不消耗魔法，随机打出战力值50%-70%的攻击力
		propertion = random.randint(50, 70) / 100
		attack_power = self._pw * propertion
		target.fixedhp(-attack_power)

	def status(self):
		#当前状态
		return '%s当前的血量为%.2f' % (self._name, self._hp)

def is_alive(monsters):
	#判断怪兽是否还有存活
	for m in monsters:
		if m.is_alive:
			return True
	return False

def rand_monster(monsters):
	#随机选择一只存活的小怪兽
	l = len(monsters) - 1
	while True:
		index = random.randint(0, l)
		target = monsters[index]
		if target.is_alive:
			return 	target

def show_status(ultraman, monsters):
	print(ultraman.status())
	for m in monsters:
		print(m.status())
	print('-----------------')

def main():
	#一只凹凸曼大战三只小怪兽
	ultraman = Ultraman('迪加', 1000, 500, 800)
	monsters = [Monster('哥尔赞', 300, 80), Monster('加库玛', 200, 70), Monster('立加德隆', 150, 100)]

	times = 1
	show_status(ultraman, monsters)
	while is_alive(monsters) and ultraman.is_alive:
		print('第%d回合：' % times)
		times += 1
		#凹凸曼随机攻击一只小怪兽
		ultraman.attack(rand_monster(monsters))
		#小怪兽同时攻击凹凸曼
		for m in monsters:
			if m.is_alive:
				m.attack(ultraman)
		#查看各自状态
		show_status(ultraman, monsters)

	if ultraman.is_alive:
		print('%s最终战胜了怪兽' % ultraman.name)
	else:
		print('%s被击败了！' % ultraman.name)

if __name__ == '__main__':
	main()