N, K = map(int,input().split())

#最短経路で行くと2N-2回の移動で行ける
#つまりKは2N-2より大きい必要がある
def judge(N, K) :
    if K < 2* N -2 :
        return False
    else :
        if K % 2 == 0 :
            return True
        else :
            return False
        
    
print('Yes' if judge(N, K) else 'No')
