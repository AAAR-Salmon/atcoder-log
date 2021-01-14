A,B = map(int,input().split())
ans = 0
for i in range(A,B+1):
	d = [i%10, i//10%10, i//100%10, i//1000%10, i//10000]
	if d[0] == d[-1] and d[1] == d[-2]:
		ans += 1
print(ans)
