H,W = map(int,input().split())
S = [input() for _ in range(H)]
ans = 0
for i in range(1,H-1):
	for j in range(1,W-1):
		tl, tc, tr = S[i-1][j-1], S[i-1][j], S[i-1][j+1]
		ml, mc, mr = S[i][j-1],   S[i][j],   S[i][j+1]
		bl, bc, br = S[i+1][j-1], S[i+1][j], S[i+1][j+1]
		if mc == '.':
			if tl == tc == ml == '#':
				ans += 1
			if tc == tr == mr == '#':
				ans += 1
			if bl == bc == ml == '#':
				ans += 1
			if bc == br == mr == '#':
				ans += 1
		if mc == '#':
			if tl == tc == ml == '.':
				ans += 1
			if tc == tr == mr == '.':
				ans += 1
			if bl == bc == ml == '.':
				ans += 1
			if bc == br == mr == '.':
				ans += 1
print(ans)
