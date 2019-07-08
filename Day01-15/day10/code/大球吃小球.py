# 在点击鼠标的位置创建颜色、大小和移动速度都随机的小球
#随机大小|颜色|速度方向；位置根据鼠标位置确定
from random import randint
import pygame
import math

class Color():
	RED = (255, 0, 0)
	GREEN = (0, 255, 0)
	BLUE = (0, 0, 255)
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	GRAY = (242, 242, 242)

	@staticmethod
	def randColor():
		r = randint(0, 255)
		g = randint(0, 255)
		b = randint(0, 255)
		return (r, g, b)

class Ball():
	"""docstring for Ball"""
	def __init__(self, x, y, r, dx, dy, color=Color.randColor()):
		self.x = x
		self.y = y
		self.r = r
		self.dx = dx
		self.dy = dy
		self.color = color
		self.alive = True

	#绘制此球
	def draw(self, screen):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.r, 0)

	#移动
	def move(self, screen):
		self.x += self.dx
		self.y += self.dy
		#超出边界时反弹
		if self.x - self.r <= 0 or self.x + self.r >= screen.get_width():
			self.dx = -self.dx
		if self.y - self.r <= 0 or self.y + self.r >= screen.get_height():
			self.dy = -self.dy

	#碰撞检测+吃或被吃
	def eat(self, other):
		if not self.alive or not other.alive or self == other:
			return False

		d = math.sqrt((self.x-other.x) ** 2 + (self.y-other.y) ** 2)
		index = self.r - other.r

		if d <= self.r + other.r:
			if index == 0:
				self.x = -self.x
				self.y = -self.y
				other.x = -other.x
				other.y = -other.y
			else:
				if index > 0:
					bigger = self
					smaller = other
				else:
					bigger = other
					smaller = self
				bigger.r = int(math.sqrt(bigger.r ** 2 + smaller.r ** 2))
				smaller.alive = False

	#随机创建
	def randball(x=0, y=0):
		r = randint(10, 100)
		dx, dy = randint(-10, 10),  randint(-10, 10)
		color = Color.randColor()
		return Ball(x, y, r, dx, dy, color)

def main():
	#初始化
	balls = [] #定义用来装所有球的容器
	pygame.init()
	mode_width, mode_height = 800, 600
	screen = pygame.display.set_mode((mode_width, mode_height))
	pygame.display.set_caption('Bigger ball eat smaller')
	running = True
	flash_time = 50 #刷新间隔ms
	create_time = 2000 #创建间隔ms
	times = 0 #刷新次数

	#循环处理事件
	while running:
		times += 1
		#从消息队列中获取事件并处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			#鼠标左键点击事件:根据点击位置随机创建
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				x, y = event.pos
				ball = Ball.randball(x, y)
				balls.append(ball)
		#渲染
		screen.fill((255, 255, 255))
		#每隔1s自动生成一球
		if times == create_time // flash_time:
			x, y = randint(0, mode_width), randint(0, mode_height)
			ball = Ball.randball(x, y)
			balls.append(ball)
			times = 0
		#取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
		for ball in balls:
			if ball.alive:
				ball.draw(screen)
			else:
				balls.remove(ball)

		pygame.display.flip()
		# 每隔50毫秒就改变球的位置再刷新窗口
		pygame.time.delay(flash_time)
		for ball in balls:
			ball.move(screen)
			# 检查球有没有吃到其他的球
			for other in balls:
				ball.eat(other)

if __name__ == '__main__':
	main()
