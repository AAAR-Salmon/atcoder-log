#include <stdio.h>
#include <math.h>

int main() {
	double A, B, H, M;
	scanf("%lf%lf%lf%lf", &A, &B, &H, &M);
	printf("%.15lf\n", sqrt(A * A + B * B - 2 * A * B * cos(M_PI / 6 * H + M_PI / (6 * 60) * M - M_PI / 30 * M)));
}
