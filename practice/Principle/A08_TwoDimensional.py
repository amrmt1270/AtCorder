H, W = map(int, input().split())
X = []
for h in range(H):
    X.append(list(map(int, input().split())))

cum = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(1, H + 1) :
    for w in range(1, W + 1):
        cum[h][w] = cum[h][w-1] + X[h-1][w-1]

for h in range(1, H + 1):
    for w in range(1, W + 1):
        cum[h][w] += cum[h-1][w]

Q = int(input())

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    ans = cum[C][D] - cum[A - 1][D] - cum[C][B - 1] + cum[A - 1][B - 1]
    print(ans)