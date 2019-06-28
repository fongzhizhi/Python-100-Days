import random

class  PokerCard():
	"""PokerCard
		list:可选，通过cards组成的列表进行初始化,'hole'初始化整副牌
		numArr:可选，通过固定顺序的card数量进行初始化
		不填参数默认整副牌
	"""
	def __init__(self, lists=[]):
		cardskey = ['3', '4', '5', '6', '7', '8', '9' ,'10', 'J', 'Q', 'K', 'A', '2', 'BJ', 'RJ']
		obj = {} #cards字典
		weight = {} #card权重
		index = 0

		if lists != 'hole':
			for key in cardskey:
				obj[key] = 0
				weight[key] = index
				index += 1
			for card in lists:
				if card in obj:
					obj[card] += 1
		else:
			numArr = [4] * (len(cardskey) - 2)
			numArr.append(1)
			numArr.append(1)
			for key in cardskey:
				obj[key] = numArr[index]
				weight[key] = index
				index += 1

		self._allkey = cardskey
		self._cardsobj = obj
		self._weight = weight

	@property
	#字典化
	def card_obj(self):
		return self._cardsobj

	@property
	#列表化(按权重排好序的)
	def card_list(self):
		clist = []
		for k in self._cardsobj:
			for x in range(0, self._cardsobj[k]):
				clist.append(k)
		return clist

	#打印
	def __str__(self):
		s =  ''
		for x in self.card_list:
			s += x + ','
		return s[0:len(s) -1]

	#获取权重
	def getWeight(self, key):
		key = str(key)
		return self._weight[key] or 0

class Rules():
	"""Play Rules"""
	def __init__(self):
		pass

	#洗牌
	@staticmethod
	def shuffle(lst):
		random.shuffle(lst) #随机排序lst(注:改变原lst)

	#发牌:返回3组牌以及,3张地主牌
	@staticmethod
	def Licensing(lst):
		result = []
		aver = len(lst) // 3 - 1
		result = [0] * 4
		start = 0
		end = aver
		for x in range(0,4):
			if x == 3:
				result[x] = lst[start: start+3]
			else:
				result[x] = lst[start:end]
			start = end
			end += aver
		return result

	#抢地主:返回下标
	@staticmethod
	def grab(players, there_card):
		max_index = random.randint(0, 2)
		allowList = [0, 1, 2, 3]
		max_point = players[max_index].callPoint(allowList)
		
		if max_point == 3:
			players[max_index].push(there_card)
			return max_index
		elif max_point in allowList and max_point == 2 or max_point == 1:
			allowList.remove(max_point)
		
		if max_index == 0:
			second = 1
			third = 2
		elif max_index == 1:
			second = 2
			third = 0
		else:
			second = 0
			third = 1

		now_point = players[second].callPoint(allowList)
		if now_point == 3:
			players[second].push(there_card)
			return second
		if now_point > max_point:
			max_index = now_point
			max_index = second
		if max_point in allowList and max_point == 2 or max_point == 1:
			allowList.remove(max_point)

		now_point = players[third].callPoint(allowList)
		if now_point == 3 or now_point > max_point:
			players[third].push(there_card)
			return third
		else:
			players[max_index].push(there_card)
			return max_index




class Player():
	"""Player
		name:昵称
		card:牌
		mates:队友
		is_robot:机器人
	"""
	def __init__(self, name, card, mates = [], is_robot = False):
		self.name = name
		self.card = card
		self.mates = mates
		self.is_robot = is_robot

	#抓牌(多张)
	def push(self, cards):
		for card in cards:
			if card in self.card.card_obj:
				self.card.card_obj[card] += 1

	#出牌(多张)
	def pop(self, cards):
		for card in cards:
			if card in self.card.card_obj:
				self.card.card_obj[card] -= 1
				if self.card.card_obj[card] < 0:
					self.card.card_obj[card] = 0

	def callPoint(self, allowList):
		if self.is_robot:
			num = random.choice(allowList)
		else:
			num = -1
			while num not in allowList:
				s = allowList.__str__()
				print('请从%s中选择一个数字进行叫分抢地主:' % s[1:len(s)-1])
				num = int(input())
		print('%s:%d分' % (self.name, num))
		return num;

	
def main():
	#整副牌,洗牌
	holeCard = PokerCard('hole').card_list
	Rules.shuffle(holeCard)
	ok_cards = Rules.Licensing(holeCard)
	there_card = ok_cards[3] #地主牌
	#初始化三个玩家，并发牌
	print('游戏开始，发牌中...')
	name = input('what\'s your name:')
	player = Player(name, PokerCard(ok_cards[0]))
	c1 = Player('C1', PokerCard(ok_cards[1]))
	c2 = Player('C2', PokerCard(ok_cards[2]))
	c1.is_robot = True
	c2.is_robot = True
	print('你拿到的牌为：')
	print(player.card)
	#抢地主
	player = [player, c1, c2]
	load_index = Rules.grab(player, there_card)
	print('%s抢到了地主，地主牌为%s' % (player[load_index].name ,there_card.__str__()))
	






if __name__ == '__main__':
	main()