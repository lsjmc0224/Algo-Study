def bfs(si, sj, ei, ej):
    v = [[0]*N for _ in range(N)]
    q = []

    v[si][sj] = 1
    q.append((si, sj))

    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            return v[ci][cj]-1

        for di, dj in ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
    return -1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # arr = [[0]*N for _ in range(N)]
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())

    ans = bfs(si, sj, ei, ej)
    print(ans)