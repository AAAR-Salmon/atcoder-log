N = int(input())
S = {}
for i in range(N):
	hash = 0
	for c in input():
		# ord('a') == 97
		hash += 11 ** (ord(c) - 97)
	if hash in S:
		S[hash] += 1
	else:
		S[hash] = 1
ans = 0
for v in S.values():
	ans += v * (v-1) // 2
print(ans)
