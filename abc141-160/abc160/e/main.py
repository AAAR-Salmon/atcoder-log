X,Y,A,B,C = map(int, input().split())
p,q = (sorted(map(int, input().split()))[-R:] for R in [X,Y])
r = list(map(int, input().split()))
print(sum(sorted(p + q + r)[-(X+Y):]))
