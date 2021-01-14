x,y=map(int,input().split())
a=0
if x + y == 2:
  a += 400000
if x <= 3:
  a += (4-x) * 100000
if y <= 3:
  a += (4-y) * 100000
print(a)
