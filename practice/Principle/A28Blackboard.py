N = int(input())
answer = 0
for i in range(N) :
    T, A = map(str, input().split())
    A = int(A)
    if T == '+' :
        answer += A
    elif T == '-' :
        answer -= A
    else :
        answer *= A
    answer %= 10000
    print(answer)