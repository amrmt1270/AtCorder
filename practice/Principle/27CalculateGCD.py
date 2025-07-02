A, B = map(int, input().split())

def calculateGCD(A, B) :
    A, B = max(A,B), min(A, B)
    while B >= 1:
        C = A % B
        A = B
        B = C
    return A

print(calculateGCD(A, B))