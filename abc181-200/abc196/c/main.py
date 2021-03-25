N = input()
N_num = int(N)
N_len = len(N)

ans = 0

if N_len % 2 == 0:
	ans = max(
		max(
			min(
				int(N[:N_len // 2]),
				int(N[N_len // 2:])
			),
			int(N[:N_len // 2]) - 1
		) - 10 ** (N_len // 2 - 1) + 1,
		0
	)

for i in range(1, (N_len + 1) // 2):
	ans += (10 ** i - 1) - 10 ** (i - 1) + 1

print(ans)
