N, x = map(int, input().split())
ans = 0

for i in range(1, N-1):
    for j in range(i+1, N):
        for k in range(j+1, N+1):
            if i + j + k == x:
                ans += 1

print(ans)