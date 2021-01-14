from functools import reduce
N=int(input())
p=[int(input()) for _ in range(N)]
sum=reduce(lambda a,b:a+b, p)
M=max(p)
print(sum - M + M // 2)
