A,B = map(int,input().split())
ans = 1
for i in range(1,B+1):
	if B // i - (A + i - 1) // i + 1 >= 2:
		ans = i
print(ans)
