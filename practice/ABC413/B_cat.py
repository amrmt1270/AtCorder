N = int(input())
s = [None] * N
for i in range(N) :
    s[i] = str(input())


answer = []
for i in range(N):
    for j in range(N) :
        if i == j :
            pass
        else:
            c = s[i] + s[j]
            answer.append(c)
answer = len(set(answer))
print(answer)