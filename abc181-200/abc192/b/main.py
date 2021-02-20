S = input()
answer = 'Yes'
for i in range(len(S)):
	if i % 2 == 0 and S[i].isupper() or i % 2 == 1 and S[i].islower():
		answer = 'No'
		break
print(answer)
