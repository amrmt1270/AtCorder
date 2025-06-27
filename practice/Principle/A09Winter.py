H, W, N = map(int, input().split())
A,B,C,D = [0] * N,[0] * N,[0] * N,[0] * N

cum = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())
    cum[A[i]][B[i]] += 1
    cum[A[i]][D[i] +1] -= 1
    cum[C[i] +1][B[i]] -= 1
    cum[C[i]+1][D[i]+1] += 1 

z = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(1, H+1):
    for j in range(1, W+1):
        z[i][j] = z[i][j-1] + cum[i][j]

for j in range(1, W +1):
    for i in range(1, H + 1):
        z[i][j] = z[i-1][j] + z[i][j]

for i in range(1, H+1):
	for j in range(1, W+1):
		if j >= 2:
			print(" ", end="")
		print(z[i][j], end="")
	print("")

