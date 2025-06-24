N = int(input())
A = [0] * N
B = [0] * N

for i in range(N) :
    A[i], B[i] = map(int, input().split())

total_distance = [0] * N

def cal_distance(start, goal):
    distance = 0
    for i in range(N):
        distance = distance + abs(A[i] -start)
        distance = distance + abs(B[i] - A[i])
        distance = distance + abs(goal - B[i])
    return distance


distance_list = []
for start in A:
    for goal in B :
        distance = cal_distance(start, goal)
        distance_list.append(distance)
ans = min(distance_list)
print(ans)