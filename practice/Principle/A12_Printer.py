N, K = map(int, input().split())

A = list(map(int, input().split()))
#x 秒で実現可能か？
def check(x, N, K, A):
    count= 0
    for i in range(N):
        count += x //A[i]
    if count >= K :
        return True
    return False
#leftは常に実現不可能な値
left = 0
#rightは常に実現可能な値
right = 10 ** 9
while right > left:
    mid = (left + right)//2
    if check(mid, N,K, A) == True:
        right = mid
    if check(mid, N, K, A) == False:
        left = mid + 1
print(left)
