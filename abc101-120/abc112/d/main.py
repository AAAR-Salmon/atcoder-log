N,M = map(int,input().split())
D = []
i = 1
while i * i < M:
	if M % i == 0:
		D.append(i)
		D.append(M // i)
	i += 1
if M % i == 0:
	D.append(i)
ans = 1
for d in D:
	if N * d <= M and M % d == 0:
		if d > ans:
			ans = d
print(ans)
