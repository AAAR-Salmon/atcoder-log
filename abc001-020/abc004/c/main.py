N = int(input())
card = bytearray(b'123456')
for i in range(N % 30):
	card[i % 5], card[i % 5 + 1] = card[i % 5 + 1], card[i % 5]
print(bytes(card).decode())
