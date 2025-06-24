#全探索であり得るパターをすべて計算
#N^2 通りの計算を行うため計算時間はO(N^2)

N, S = map(int, input().split())
blue = [i+1 for i in range(N)]
red = [j+1 for j in range(N)]

ans = 0
for card1 in blue:
    for card2 in red:
        if card1 + card2 <= S:
            ans +=1

print(ans)