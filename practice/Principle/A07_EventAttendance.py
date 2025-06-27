D = int(input())
N = int(input())

diff = [0] * (D+2)
cum = [0] * (D+2)

for i in range(1, N+1):
    L, R = map(int, input().split())
    diff[L] += 1
    diff[R+1] -= 1

for d in range(1, D+1):
    cum[d] = cum[d-1] + diff[d]
    print(cum[d])


