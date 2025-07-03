D, N = map(int,input().split())
L, R, H = [None] * N, [None] * N, [None] * N
LIM = [24] * (D +1)

total = 0
for i in range(N) :
    L[i], R[i], H[i] = map(int,input().split())
    for d in range(L[i], R[i] +1) :
        LIM[d] = min(LIM[d], H[i])

total = sum(LIM[1:])
print(total)