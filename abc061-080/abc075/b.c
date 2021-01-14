#include <stdio.h>

int main(void) {
	int H, W;
	scanf("%d%d", &H, &W);
	char S[H][W];
	for (int i = 0; i < H; i++) {
		scanf("%s", S[i]);
	}

	for (int i = 0; i < H; i++) {
		for (int j = 0; j < W; j++) {
			if (S[i][j] == '#') {
				putchar('#');
			} else {
				int n = 0;
				for (int dy = -1; dy <= 1; dy++) {
					int y = i + dy;
					for (int dx = -1; dx <= 1; dx++) {
						int x = j + dx;
						if (y < 0 || y >= H || x < 0 || x >= W) {
							continue;
						}
						if (S[y][x] == '#') {
							n++;
						}
					}
				}
				putchar('0' + n);
			}
		}
		putchar('\n');
	}
	return 0;
}
