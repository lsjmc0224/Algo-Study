def bfs(si, sj):
    q = []
    v = [[0]*(M) for _ in range(N)]

    v[si][sj] = 1
    q.append((si, sj)) # queue에다가 시작 지점을 넣어주고 시작

    while q:
        ci, cj = q.pop(0)
        if (ci+1, cj+1) == (N, M):
            return v[ci][cj]

        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and maze[ni][nj] != 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

si, sj = 0, 0
ans = bfs(si, sj)
print(ans)