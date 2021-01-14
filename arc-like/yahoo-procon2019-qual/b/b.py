n=[0]*4
for _ in range(3):
	a,b=map(int,input().split())
	n[a-1] += 1
	n[b-1] += 1
ok = True
for i in range(4):
	if n[i] > 2:
		ok = False
print('YES' if ok else 'NO')
