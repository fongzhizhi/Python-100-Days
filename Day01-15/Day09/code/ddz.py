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

	#抢地主:返回下标(重复代码过多，可优化)
	@staticmethod
	def grab(players, there_card):
		max_index = random.randint(0, 2)
		allowList = [0, 1, 2, 3]
		max_point = players[max_index].callPoint(allowList)
		
		if max_point == 3:
			players[max_index].push(there_card)
			return max_index
		elif max_point in allowList and (max_point == 2 or max_point == 1):
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
		if max_point in allowList and (max_point == 2 or max_point == 1):
			allowList.remove(max_point)

		now_point = players[third].callPoint(allowList)
		if now_point == 3 or now_point > max_point:
			players[third].push(there_card)
			return third
		else:
			players[max_index].push(there_card)
			return max_index

	@staticmethod
	def fixed_index(now_index):
		index = now_index
		if now_index > 2:
			index = now_index % 3
		elif now_index < 0:
			index = -index
			index = Rules.fixed_index(index)
		return index

	@staticmethod
	def getKindOfCards(cards):
		kind = -1
		l = len(cards)
		if l == 0 or l == 1:
			kind = l
		elif l == 2 and cards[0] == cards[1]:
			kind = l
		elif l == 3 and cards[0] == cards[1] and cards[0] == cards[2]:
			kind = l
		elif l == 4 and cards[0] == cards[1] and cards[0] == cards[2] and cards[2] == cards[3]:
			kind = l
		return kind

	@staticmethod
	def getWeightOfCards(cards, pc):
		return pc.getWeight(cards[0])

	@staticmethod
	def auto_play(cards, last_i, now_i, players):
		result = [cards, last_i]
		if len(cards) == 0 or players[last_i].name == players[now_i].name:
			#自由出牌
			kind = 0
			weight = -1
		else:
			#根据大小出
			kind = Rules.getKindOfCards(cards)
			weight = Rules.getWeightOfCards(cards, players[now_i].card)

		min_card = players[now_i].get_min_weight_cards(kind, weight)
		if len(min_card) > 0:
			result[0] = min_card
			result[1] = now_i
		return result

	@staticmethod
	def another_index(players, now_i):
		while True:
			now_i += 1
			now_i = Rules.fixed_index(now_i)
			if not players[now_i].is_load:
				return now_i

class Player():
	"""Player
		name:昵称
		card:牌
		is_robot:机器人
		is_load:地主
	"""
	def __init__(self, name, card, is_robot = False, is_load = False):
		self.name = name
		self.card = card
		self.is_robot = is_robot
		self.is_load = is_load
	
	@property
	def cardnum(self):
		return len(self.card.card_list)

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
	def get_min_weight_cards(self, kind, weight=-1):
		if kind < 0:
			return []
		if kind == 0:
			for card in self.card.card_obj:
				l = self.card.card_obj[card]
				if l > 0:
					return [card] * l
		result = []
		for card in self.card.card_obj:
			l = self.card.card_obj[card]
			if l > kind-1 and self.card.getWeight(card) > weight:
				result = [card] * kind
				break;
		return result
	
def main():
	#整副牌,洗牌
	holeCard = PokerCard('hole').card_list
	Rules.shuffle(holeCard)
	ok_cards = Rules.Licensing(holeCard)
	there_card = ok_cards[3] #地主牌
	#初始化三个玩家，并发牌
	name = input('what\'s your name:')
	print('【游戏开始，发牌中...】')
	player = Player(name, PokerCard(ok_cards[0]))
	c1 = Player('C1', PokerCard(ok_cards[1]))
	c2 = Player('C2', PokerCard(ok_cards[2]))
	c1.is_robot = True
	c2.is_robot = True
	print('你拿到的牌为：')
	print(player.card)
	#抢地主
	print('【开始抢地主...】')
	players = [player, c1, c2]
	now_index = Rules.grab(players, there_card)
	players[now_index].is_load = True
	print('%s抢到了地主，地主牌为%s' % (players[now_index].name ,there_card.__str__()))
	last_cards = []
	last_index = now_index
	play_result = []
	gameover = False
	#战斗
	while not gameover:
		#robot auto playing
		if players[now_index].is_robot:
			play_result = Rules.auto_play(last_cards, last_index, now_index, players)
		else:
			play_result = Rules.auto_play(last_cards, last_index, now_index, players)

		last_cards = play_result[0]
		last_index = play_result[1]
		if last_index == now_index and len(last_cards) > 0:
			players[now_index].pop(last_cards)
			cards_str = last_cards.__str__()
			print('%s: %s' % (players[now_index].name, cards_str[1:len(cards_str)-1]))
		else:
			print('%s: 过!' % players[now_index].name)
		
		if players[now_index].cardnum <= 0:
			gameover = True
		else:
			now_index += 1
			now_index = Rules.fixed_index(now_index)
	#战况
	if players[now_index].is_load:
		print('【游戏结束，地主%s获胜!】' % players[now_index].name)
	else:
		print('【游戏结束，%s和%s获胜!】' % (players[now_index].name, players[Rules.another_index(players, now_index)].name))
	
	for p in players:
		print('%s剩余的牌为:' % p.name)
		print(p.card)

if __name__ == '__main__':
	main()