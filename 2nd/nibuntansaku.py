#二分探索を行う
#長さNの正数列A0-A_N-1 が与えられたときこの正数列は小さい値から順に並ぶようにソートされている
#また整数Kが与えられているときA_i >= K であるようなもののうち最小の物を出力して下さい。そのようなものがないときは-1を返して下さい


N, K = map(int, input().split())
A = list(map(int, input().split()))

def binary_search(N, A, K):
    left = -1
    right = N 
    while right - left > 1:
        mid = (right + left)//2
        if A[mid] >= K:
            right = mid 
        else :
            left = mid 
    return right if right < N else -1


print(binary_search(N,A,K))