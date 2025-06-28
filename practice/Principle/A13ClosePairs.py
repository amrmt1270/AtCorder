N, K = map(int, input().split())
A = list(map(int, input().split()))


#解放1　二分探索法
count = 0

for i in range(N):
    left = i + 1  # j > i
    right = N
    while left < right:
        mid = (left + right) // 2
        if A[mid] - A[i] <= K:
            left = mid + 1
        else:
            right = mid
    count += left - (i + 1)  # i+1 〜 left-1 が条件を満たす

print(count)

#解放2 しゃくとり法
N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
R = [0] * N
for i in range(N-1) :
    if i == 0 :
        R[i] = 0
    else:
        R[i] = max(R[i-1], i)
    while R[i] + 1 < N and A[R[i] + 1] - A[i] <= K :
        R[i] += 1
        count += R[i] - i 

print(count)