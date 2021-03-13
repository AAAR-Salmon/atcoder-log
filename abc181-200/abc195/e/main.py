N = int(input())
S = list(map(int,input()))
X = input()
T = 0
for i in range(N):
	if X[-i-1] == 'A':
		if T == 0:
			T = (T + S[-i-1] * pow(10, S[-i-1], 7)) % 7
	else:
		if (T + S[-i-1] * pow(10, S[-i-1], 7)) % 7 == 0:
			T = (T + S[-i-1] * pow(10, S[-i-1], 7)) % 7
print('Takahashi' if T == 0 else 'Aoki')
