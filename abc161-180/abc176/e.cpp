#include <cstdio>
#include <unordered_set>
#include <utility>
using namespace std;
using ll = long long;

struct phash {
	inline size_t operator()(const pair<int, int> &p) const {
		const auto h1 = hash<int>()(p.first);
		const auto h2 = hash<int>()(p.second);
		return h1 ^ (h2 << 1);
	}
};

int main() {
	int H, W, M;
	scanf("%d%d%d", &H, &W, &M);
	unordered_set<pair<int, int>, phash> tg;
	int *sumr, *sumc;
	sumr = new int[H]();
	sumc = new int[W]();
	for (int i = 0; i < M; i++) {
		int h, w;
		scanf("%d%d", &h, &w);
		h--, w--;
		tg.insert(make_pair(h, w));
		sumr[h]++;
		sumc[w]++;
	}

	unordered_set<int> maxi, maxj;
	int maxsumr = 0, maxsumc = 0;
	for (int i = 0; i < H; i++) {
		if (sumr[i] > maxsumr) {
			maxi.clear();
			maxsumr = sumr[i];
			maxi.insert(i);
		} else if (sumr[i] == maxsumr) {
			maxi.insert(i);
		}
	}
	for (int j = 0; j < W; j++) {
		if (sumc[j] > maxsumc) {
			maxj.clear();
			maxsumc = sumc[j];
			maxj.insert(j);
		} else if (sumc[j] == maxsumc) {
			maxj.insert(j);
		}
	}
	ll n = maxi.size() * maxj.size();
	for (auto p : tg) {
		if (maxi.count(p.first) && maxj.count(p.second)) {
			n--;
		}
		if (n == 0) {
			break;
		}
	}
	printf("%d\n", maxsumr + maxsumc - (n == 0));
	return 0;
}
