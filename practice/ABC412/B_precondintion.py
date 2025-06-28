S = str(input())
T = str(input())

upper_s = S.upper()
c_list = []

for i in range(1, len(S)):
    if S[i] == upper_s[i] :
        c_list.append(S[i-1])

answer = 'Yes'
for c in c_list:
    if c not in T:
        answer = 'No'
        break

print(answer)