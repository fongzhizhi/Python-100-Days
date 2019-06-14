'''
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次摇色子 如果摇出7点 庄家胜，如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束
'''
from random import randint

money = 1000 #本钱
each = 100 #赌注(TODO：可改为每次玩家下注)
times = 0 #游戏次数
eachtimes = 0 #单局掷骰子次数
new = True #新的一局

##规则
print('Craps赌博游戏规则如下：')
print()
print('---------------------')
print('1.玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜')
print('2.如果摇出2点 3点 12点 庄家胜 其他情况游戏继续')
print('3.玩家再次摇色子 如果摇出7点 庄家胜，如果摇出第一次摇的点数 玩家胜')
print('4.平局继续规则3')
print('---------------------')
print()

command = input('您共有1000大洋作为本金，请输入1开始游戏，输入0退出游戏：')

while command != '':
	if command == '1':
		while command == '1':
			if money <= 0:
				command = '0'
				print('你已经输光！！！')
				break
			if new:
				times += 1
			eachtimes += 1
			dice1 = randint(1,6)
			dice2 = randint(1,6)
			diceSum = dice1 + dice2
			print('您掷骰子的点数为%d，%d，总点数为%d' % (dice1, dice2, diceSum), end='，')
			if eachtimes == 1:
				flag = diceSum #第一次的点数
				if diceSum == 7 or diceSum == 12:
					print('【玩家获胜】！')
					print('------')
					money += each
					new = True
				elif diceSum == 2 or diceSum == 3 or diceSum == 12:
					print('【庄家获胜】！')
					print('------')
					money -= each
					new = True
				else:
					print('平局！')
					new = False
				command = input('继续游戏请输入1，退出游戏输入0：')
			else:
				if diceSum == flag:
					print('【玩家获胜】！')
					print('------')
					money += each
					new = True
				elif diceSum == 7:
					print('【庄家获胜】！')
					print('------')
					money -= each
					new = True
				else:
					print('平局！')
					new = False
				command = input('继续游戏请输入1，退出游戏输入0：')

	elif command == '0':
		break;
	else:
		command = input('请输入正确指令：')

print('Game Over!您一共赌博了%d次，余额为%d.' % (times, money))
