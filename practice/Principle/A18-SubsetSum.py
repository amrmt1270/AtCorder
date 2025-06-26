N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N+1)]

dp[0][0] = True
for i in range(1, N + 1):
    for j in range(0, S + 1):
        if dp[i-1][j] == True:
            dp[i][j] = True
        if j >= A[i-1] and dp[i-1][j-A[i-1]] :
            dp[i][j] = True

print("Yes" if dp[N][S] else "No")