N=int(input())
y=False
for i in range(1,10):
  if N // i <= 9 and N % i == 0: y=True
print('Yes' if y else 'No')
