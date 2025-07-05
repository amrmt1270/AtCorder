from fractions import Fraction
from itertools import permutations
T = int(input())

def is_geometric_any_order(arr):
    if len(arr) <= 2:
        return True
    for perm in permutations(arr):
        r = Fraction(perm[1], perm[0]) if perm[0] != 0 else None
        if r is None:
            continue
        valid = True
        for i in range(2, len(perm)):
            if perm[i - 1] == 0 or Fraction(perm[i], perm[i - 1]) != r:
                valid = False
                break
        if valid:
            return True
    return False

for t in range(T) :
    N = int(input())
    A = list(map(int, input().split()))
    print('Yes' if is_geometric_any_order(A) else 'No')