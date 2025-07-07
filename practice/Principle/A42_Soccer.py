
N, K = map(int, input().split())

A =[0]*N
B = [0]*N
for i in range(N):
    A[i], B[i] = map(int,input().split())

#下限値が決まった時に何員が参加できるかをカウント
def get_num(a, b):
    count = 0
    for i in range(N) :
        if a <= A[i] <= a + K and b <= B[i] <= b + K :
            count += 1
    return count


#下限値を全探索
max_count = 0
for a in range(100) :
    for b in range(100) :
        count = get_num(a,b)
        max_count = max(count, max_count)

print(max_count)