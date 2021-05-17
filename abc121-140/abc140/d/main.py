N,K = map(int,input().split())
S = input()
Scomp = []
p = S[0]
n = 1
for c in S[1:]:
	if p == c:
		n += 1
	else:
		Scomp.append((p, n))
		p = c
		n = 1
Scomp.append((p, n))

group = len(Scomp)
for _ in range(K):
	if group >= 3:
		group -= 2
	elif group == 2:
		group = 1

print(N - group)
