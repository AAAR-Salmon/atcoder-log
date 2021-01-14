#include <assert.h>
#include <stdlib.h>

void swap(int *x, int *y) {
  int tmp;
  tmp = *x;
  *x = *y;
  *y = tmp;
}

typedef struct {
  int _n;
  int *parent;
} UnionFind;

UnionFind make_unionfind(int n) {
  UnionFind uf;
  uf._n = n;
  uf.parent = (int *)malloc(sizeof(int) * n);
  for (int i = 0; i < n; i++) {
    uf.parent[i] = -1;
  }
  return uf;
}

void delete_unionfind(UnionFind *ufp) { free(ufp->parent); }

int find(UnionFind *ufp, int i) {
  assert(0 <= i && i < ufp->_n);
  if (ufp->parent[i] < 0) {
    return i;
  } else {
    return ufp->parent[i] = find(ufp, ufp->parent[i]);
  }
}

int merge(UnionFind *ufp, int i, int j) {
  assert(0 <= i && i < ufp->_n);
  assert(0 <= j && j < ufp->_n);
  int x, y;
  x = find(ufp, i);
  y = find(ufp, j);
  if (x == y) {
    return x;
  }
  if (-ufp->parent[x] < -ufp->parent[y]) {
    swap(&x, &y);
  }
  ufp->parent[x] += ufp->parent[y];
  return ufp->parent[y] = x;
}

int size(UnionFind uf) { return uf._n; }

int size_group(UnionFind *ufp, int i) {
  assert(0 <= i && i < ufp->_n);
  return -ufp->parent[find(ufp, i)];
}

int count_group(UnionFind uf) {
  int result = 0;
  for (int i = 0; i < uf._n; i++) {
    if (uf.parent[i] < 0) {
      result++;
    }
  }
  return result;
}
