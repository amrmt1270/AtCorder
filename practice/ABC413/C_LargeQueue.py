from collections import deque

Q = int(input())
A = deque()  # (value, count)
total = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, c = query[1], query[2]
        A.append((c, x))
    else:
        x = query[1]
        s = 0
        while x > 0:
            v, cnt = A[0]
            if cnt <= x:
                s += v * cnt
                x -= cnt
                A.popleft()
            else:
                s += v * x
                A[0] = (v, cnt - x)
                x = 0
        print(s)
