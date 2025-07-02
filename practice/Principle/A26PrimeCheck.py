import math

def PrimeCheck(N) :
    fin = int(math.sqrt(N))
    for i in range(2, fin + 1) :
        if N % i == 0 :
            return False
    return True

Q = int(input())
for q in range(Q) :
    X = int(input())
    print('Yes' if PrimeCheck(X) else 'No')

