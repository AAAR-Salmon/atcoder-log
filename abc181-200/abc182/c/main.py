from functools import reduce
N=input()
k=len(N)
d=[0]*3
sum=0
for c in map(lambda x:int(x) % 3,list(N)):
	d[c] += 1
	sum += c
sum %= 3

ans=-1
if sum == 0:
	ans = 0
elif sum == 1:
	if d[1] >= 1 and k > 1:
		ans = 1
	elif d[2] >= 2 and k > 2:
		ans = 2
elif sum == 2:
	if d[2] >= 1 and k > 1:
		ans = 1
	elif d[1] >= 2 and k > 2:
		ans = 2
print(ans)
