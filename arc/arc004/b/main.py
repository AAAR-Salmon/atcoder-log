N = int(input())
d = [int(input()) for _ in range(N)]
print(sum(d))
print(max(max(d) * 2 - sum(d), 0))
