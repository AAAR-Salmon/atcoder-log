input()
S=input()
a=0
b=''
for c in S:
  if b != c:
    a += 1
    b = c
print(a)
