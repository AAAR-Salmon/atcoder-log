import cmath

N = int(input())
p0 = complex(*map(int,input().split()))
pn2 = complex(*map(int,input().split()))
c = (p0 + pn2) / 2
p1 = (p0 - c) * cmath.exp(2j * cmath.pi / N) + c
print(p1.real, p1.imag)
