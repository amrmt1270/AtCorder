N , K = map(int, input().split())
cum = [[0] * 102  for _ in range(102)]
for i in range(N) :
    a, b = map(int,input().split())
    cum[a + 1][b + 1] += 1

for i in range(1, 102) :
    for j in range(1, 102) :
        cum[i][j] += cum[i][j- 1]
for j in range(1, 102):
    for i in range(1, 102):
        cum[i][j] += cum[i -1 ][j]

max_count = 0
for i in range(1, 102 - K) :
    for j in range(1, 102 - K) :
        count = cum[i + K][j + K] - cum[i + K][j-1] -cum[i-1][j + K] + cum[i-1][j-1]
        max_count = max(count, max_count)

print(max_count)