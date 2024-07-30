import sys
sys.setrecursionlimit(10000)

def dfs(si, sj):
    v[si][sj] = 1

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and cab[ni][nj] == 1:
            dfs(ni, nj)


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())

    cab = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        # s가 가로에, e가 세로에 속함 / [e][s]로 탐색해야 함
        s, e = map(int, input().split())
        cab[e][s] = 1
    # 이중 for문을 통해 전체 탐색한 뒤, not visited / cab = 1 케이스

    v = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if cab[i][j] == 1 and v[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)
