N = int(input())
A = set(map(int,input().split()))

print('Yes' if all(i in A for i in range(1, N + 1)) else 'No')
