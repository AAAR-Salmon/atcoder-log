S = ''.join(reversed(input()))
S = S.replace('6', '@')
S = S.replace('9', '6')
S = S.replace('@', '9')
print(S)
