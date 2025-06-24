N, Q=map(int, input().split())
A=list(range(1, N+1))
offset=0
for q in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1 :
        p,x = query[1], query[2]
        A[((offset + p) %N) -1] = x
    elif query[0] == 2 :
        p = query[1]
        print(A[((offset + p) %N) -1])
    else:
        k = query[1]
        offset = (offset + k) %N

