import math

N=int(input())
X=list(map(int, input().split()))
man=0
euc=0
chev=0
for x in X:
    man += abs(x)
    euc += x * x
    chev = max(chev, abs(x))
print(man)
print('{:.16g}'.format(math.sqrt(euc)))
print(chev)
