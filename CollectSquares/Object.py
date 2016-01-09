import math
from Point import Point

class Object:
	def __init__(self):
		self.pos = Point(0,0)
		self.p1 = Player()
		self.p2 = Player()
		self.type = "object"

	def move(self, xamnt, yamnt):
		self.pos.x += xamnt
		self.pos.y += yamnt

	def limit_position(self, xmin, xmax, ymin, ymax):
		self.pos.x = max(self.pos.xmin, min(self.pos.xmax, self.pos.x))
		self.pos.y = max(self.pos.ymin, min(self.pos.ymax, self.pos.y))

	def collision(self, otherobj):
		if (self.pos.x + self.width < otherobj.pos.x) or (self.pos.x > otherobj.pos.x + otherobj.width):
			return False
		if (self.pos.y + self.height < otherobj.pos.y) or (self.pos.y > otherobj.pos.y + otherobj.height):
			return False
		return True

	def distance(self, otherobj, sqrt=False):
		dist = (self.pos.x - otherobj.pos.x)*(self.pos.x - otherobj.pos.x) + (self.pos.y - otherobj.pos.y)*(self.pos.x - otherobj.pos.x)
		if sqrt:
			return math.sqrt(dist)
		else:
			return dist

	def relative_position(self, toobj):
		return Point(toobj.pos.x - self.pos.x, toobj.pos.y - self.pos.y)
