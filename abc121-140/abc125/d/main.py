N = int(input())
A = list(map(int,input().split()))
if 0 in A:
	print(sum(abs(a) for a in A))
else:
	cnt_neg = sum(1 for a in A if a < 0)
	if cnt_neg % 2 == 0:
		print(sum(abs(a) for a in A))
	else:
		B = list(map(abs, A))
		print(sum(abs(b) for b in B) - min(B) * 2)
