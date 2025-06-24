A = list(map(int, input().split()))
P = int(input())
sorted_A = sorted(A)

#その数が適温となりうるかを確認する
def check_boader(boader):
    for start in range(len(A)-P+1):
        B = A[start: start+P]
        if all(temp >= boader for temp in B):
            return False
    return True

#並べ替えたリストAに対して二分探索を行う
right = len(A)
left = -1

while right - left > 1:
    mid = (right + left)//2
    if check_boader(sorted_A[mid]):
        left = mid
    else:
        right = mid

print(sorted_A[left])