n = int(input())

right = (n+1)*n/2
left = 1
while right - left > 1:
    mid = (left + right)//2
    if mid*(mid +1)//2 <= n+1:
        left = mid
    else:
        right = mid

print(int(n+1 -left))