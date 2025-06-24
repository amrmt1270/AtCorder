N, Q = map(int, input().split())
X = list(map(int, input().split()))

def cls_ball(X, N):
    B = [0] *Q
    box = [0] * N
    for i in range(Q):
        if X[i] >= 1:
            B[i] = X[i] 
            box[X[i]-1] += 1
        else:
            min_idx = box.index(min(box))
            B[i] = min_idx +1 
            box[min_idx] += 1
    
    return B

print(*cls_ball(X, N))
