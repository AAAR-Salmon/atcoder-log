S = input()
T = input()
ans = 'UNRESTORABLE'
for i in range(len(S) - len(T), -1, -1):
	if all(S[i + j] == '?' or S[i + j] == T[j] for j in range(len(T))):
		ans = list(S)
		ans[i:i+len(T)] = list(T)
		ans = ''.join(ans)
		ans = ans.replace('?', 'a')
		break
print(ans)
