S=input()
b=False
for i in range(1,6):
  if S == 'hi' * i:
    b = True
print('Yes' if b else 'No')
