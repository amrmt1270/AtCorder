#グラフの表現を隣接リスト表現で行う
#N頂点M辺の無向グラフがグラフ全体が連結であることを判定する。

N, M = map(int, input().split())
A, B = [0] * M , [0] * M
G = [list() for i in range(N + 1)]

for i in range(M):
    A[i], B[i] = map(int, input().split())
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

#i番目の頂点がGに入っているようなリストを作成している

#グラフがグリッド上で表現されているとしている
