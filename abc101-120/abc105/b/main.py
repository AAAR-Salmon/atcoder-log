N = int(input())
ans = 'No'
for i in range(0,101,4):
	for j in range(0,101,7):
		if i+j == N:
			ans = 'Yes'
print(ans)
