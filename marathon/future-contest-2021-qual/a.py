class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

k=0
n=0
ins=''
Ps=[None] * 101
Ps[0]=Point(0,0)
for i in range(100):
	x,y=map(int,input().split())
	Ps[i+1] = Point(x,y)
for i in range(100):
	dx = Ps[i+1].x - Ps[i].x
	dy = Ps[i+1].y - Ps[i].y
	ins += 'D' * dx if dx > 0 else 'U' * (-dx)
	ins += 'R' * dy if dy > 0 else 'L' * (-dy)
	k += abs(dx) + abs(dy)
	n += abs(dx) + abs(dy) + 1
	ins += 'I'
print(ins)
