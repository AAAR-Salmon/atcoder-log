MAX = 277775

is_prime = [True] * MAX
is_prime[0] = False
is_prime[1] = False
i = 2
while i * i <= MAX:
	if not is_prime[i]:
		i += 1
		continue
	j = i * 2
	while j < MAX:
		is_prime[j] = False
		j += i
	i += 1
ans = [i for i, v in enumerate(is_prime) if v and i % 5 == 1]

print(*ans[:int(input())])

