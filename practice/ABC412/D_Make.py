class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.edge_count = [0]*n

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            self.edge_count[rx] += 1
            return
        if self.size[rx] < self.size[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        self.edge_count[rx] += self.edge_count[ry] + 1

    def get_components(self):
        comp = {}
        for i in range(len(self.parent)):
            r = self.find(i)
            if r not in comp:
                comp[r] = (self.size[r], self.edge_count[r])
        return comp.values()

# 入力
N, M = map(int, input().split())
uf = UnionFind(N)

for _ in range(M):
    A, B = map(int, input().split())
    uf.union(A - 1, B - 1)

# 各成分に対して必要な操作を求める
total_ops = 0
for v_cnt, e_cnt in uf.get_components():
    total_ops += abs(v_cnt - e_cnt)

print(total_ops)
