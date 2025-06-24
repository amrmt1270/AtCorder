N, x = map(int, input().split())
ans =0
for i in range(1, N-1):
    for j in range(i+1, N):
        k = x-i-j
        if j < k <= N:
            ans += 1

print(ans)