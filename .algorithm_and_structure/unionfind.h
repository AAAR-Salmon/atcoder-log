#include <assert.h>
#include <stdlib.h>

void swap(int *x, int *y);

typedef struct {
  int _n;
  int *parent;
} UnionFind;

UnionFind make_unionfind(int n);
void delete_unionfind(UnionFind *ufp);
int find(UnionFind *ufp, int i);
int merge(UnionFind *ufp, int i, int j);
int size(UnionFind uf);
int size_group(UnionFind *ufp, int i);
int count_group(UnionFind uf);
