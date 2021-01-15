def popcount(x):
	assert(0 <= x <= 0xFFFFFFFF)
	x = x - (x >> 1 & 0x55555555)
	x = (x & 0x33333333) + (x >> 2 & 0x33333333)
	x = (x + (x >> 4)) & 0x0f0f0f0f
	x = (x + (x >> 8)) & 0x00ff00ff
	x = (x + (x >> 16)) & 0x0000ffff
	return x
