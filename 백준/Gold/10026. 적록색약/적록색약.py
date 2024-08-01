import sys
sys.setrecursionlimit(10000)

def solve(arr):
    def dfs(ci, cj):
        v[ci][cj] = 1

        for di, dj in dir:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                dfs(ni, nj)

    v = [[0]*N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                dfs(i, j)
                cnt += 1
    return cnt


N = int(input())
pic = [list(map(str, input().strip())) for _ in range(N)]
fake = [[0] * N for _ in range(N)]
dir = [(1,0), (-1,0), (0,1), (0,-1)]

for i in range(N):
    for j in range(N):
        if pic[i][j] == 'R' or pic[i][j] == 'G':
            fake[i][j] = 0
        elif pic[i][j] == 'B':
            fake[i][j] = 1

print(solve(pic), solve(fake))