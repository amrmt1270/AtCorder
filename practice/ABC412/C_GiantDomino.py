T = int(input())

#貪欲法で解く
def count_domino(N , S):
    answer = 1
    place = 0
    used = [0] * N
    while True :
        if S[place] * 2 >= S[N-1]:
            answer += 1
            break
        nxt = -1
        for i in range(1, N):
            if used[i] :
                continue
            if S[place] * 2 >= S[i]:
                if nxt != -1 and S[nxt] >= S[i]:
                    continue
        if nxt != -1 or S[nxt] <= S[place]:
            return -1
        answer += 1
        place = nxt
        used[nxt] = 1
    return answer


for t in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    print(count_domino(N,S))

