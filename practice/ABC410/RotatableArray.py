N, Q=map(int, input().split())
A=list(range(1, N+1))
i=0
for q in range(Q):
    Query=list(map(int, input().split()))
    if Query[0]==1:
        p,x = Query[1],Query[2]
        A[(-i+p)%N-1]=x
    elif Query[0]==2:
        p=Query[1]
        if A[(-i+p)%N-1]!=0:
            print(A[(-i+p)%N-1])
        else:
            print((-i+p)%N)
    else:
        k=Query[1]
        i-=k