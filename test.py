# 在点击鼠标的位置创建颜色、大小和移动速度都随机的小球
#随机大小|颜色|速度方向；位置根据鼠标位置确定
from random import randint
import pygame

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
		self.x += dx
		self.y += dy
		#超出边界时返回
		if self.x - self.r <= 0 or self.x + self.r >= screen.get_width():
			self.dx = -self.dx
		if self.y - self.r <= 0 or self.y + self.r >= screen.get_height():
			self.dy = -self.dy

	#碰撞检测+吃
	def eat(self, other):
		self
		pass