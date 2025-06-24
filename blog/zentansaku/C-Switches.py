def get_binary(x):
    if x == 0:
        return [0]

    n = 0
    while (2 ** n) <= x:
        n += 1

    binary = [0] * n
    for i in range(n):
        power = n - 1 - i  # 上位ビットから順に
        if x >= 2 ** power:
            binary[i] = 1
            x -= 2 ** power
    return binary
