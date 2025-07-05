N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
if total <= M :
    print('Yes')
else :
    print('No')

