N , M,  B = map(int, input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

total = 0
total += B * M * N
for i in range(N) :
    total += A[i] * M
for j in range(M) :
    total += C[j] * N

print(total)