#xが何個の約数を持つかカウントする関数
def count_gcd(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

N = int(input())
ans = 0
for i in range(1, N+1):
    if i % 2 == 1:
        if count_gcd(i) == 8:
            ans += 1

print(ans)