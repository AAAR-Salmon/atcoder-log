N = int(input())
S = list(map(int,input()))
X = input()
AokiWin = [[True] * 7 for _ in range(N+1)]
AokiWin[N][0] = False

p10 = 1
for i in range(N):
	if X[-1-i] == 'A':
		for j in range(7):
			AokiWin[-2-i][j] = AokiWin[-1-i][(j + S[-1-i] * p10) % 7] or AokiWin[-1-i][j]
	else:
		for j in range(7):
			AokiWin[-2-i][j] = AokiWin[-1-i][(j + S[-1-i] * p10) % 7] and AokiWin[-1-i][j]
	p10 = p10 * 10 % 7

print('Aoki' if AokiWin[0][0] else 'Takahashi')
