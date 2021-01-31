n = int(input())
v = list(map(int,input().split()))
E = [0] * 100001
O = [0] * 100001
for i in v[0::2]:
	E[i] += 1
for i in v[1::2]:
	O[i] += 1
E = sorted([(i, e) for i, e in enumerate(E)], key=lambda x: x[1], reverse=True)
O = sorted([(i, o) for i, o in enumerate(O)], key=lambda x: x[1], reverse=True)
if E[0][0] != O[0][0]:
	print(n - E[0][1] - O[0][1])
else:
	print(n - max(E[0][1] + O[1][1], E[1][1] + O[0][1]))
