import math

def compute_unique_lcms(L, R):
    lcm_list = []
    lcm = 1
    for n in range(1, R + 1):
        lcm = lcm * n // math.gcd(lcm, n)
        lcm_list.append(lcm)

    return len(set(lcm_list[L-1:R]))

L, R = map(int, input().split())
print(compute_unique_lcms(L, R))
