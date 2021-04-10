N = int(input())
a = sorted([(int(input()), i) for i in range(N)])
b = [None] * N
prev_v, prev_i = a[0]
prev_bi = 0
b[prev_i] = prev_bi
for v, i in a[1:]:
	if v == prev_v:
		b[i] = prev_bi
	else:
		prev_bi += 1
		b[i] = prev_bi
		prev_v = v
print(*b, sep='\n')
