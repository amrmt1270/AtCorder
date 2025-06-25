N = int(input())

D = list(map(int, input().split()))

total = [0] * N
for i in range(1, N):
    total[i] = total[i-1] + D[i-1]

for i in range(N-1):
    answers = []
    for j in range(i+1, N):
        ans = total[j] - total[i]
        answers.append(ans)
    print(*answers)

