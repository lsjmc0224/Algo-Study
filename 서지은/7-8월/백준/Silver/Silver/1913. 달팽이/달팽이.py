N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

num = N*N
i, j = 0, 0
ai, aj = 0, 0
d = 0

while num > 0:
    arr[i][j] = num

    if num == K:
        ai, aj = i+1, j+1

    ni, nj = i + dir[d][0], j+dir[d][1]

    if not(0<=ni<N and 0<=nj<N) or arr[ni][nj] != 0:
        d = (d+1) % 4
        ni, nj = i+dir[d][0], j+dir[d][1]

    i, j = ni, nj
    num -= 1

for lst in arr:
    print(*lst)
print(ai, aj)
