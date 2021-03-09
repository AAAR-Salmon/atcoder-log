#include <stdio.h>

int main() {
	int H, W, K;
	scanf("%d %d %d", &H, &W, &K);
	char m[H * W];
	for (int i = 0; i < H * W; i++) {
		scanf(" %c", &m[i]);
	}
	int ans = 0;
	for (int h = 0; h < 1 << H; h++) {
		for (int w = 0; w < 1 << W; w++) {
			int bn = 0;
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					if (h >> i & 1 && w >> j & 1 && m[i * W + j] == '#') {
						bn++;
					}
				}
			}
			if (bn == K) {
				ans++;
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}
