import math

N = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(max(A) + 1) :
    m = A.count(i)
    if m <= 2 :
        pass
    else :
        triangle = int(math.factorial(m) / (6 * math.factorial(m-3)))
        total += triangle
    
print(total)