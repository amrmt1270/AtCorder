N = int(input())
A =[]
for i in range(N):
    l, r = map(int, input().split())
    A.append([r, l])

A.sort()
time = 0
total = 0
for i in range(N):
    if time <=A[i][1] :
        time = A[i][0]
        total += 1
print(total)