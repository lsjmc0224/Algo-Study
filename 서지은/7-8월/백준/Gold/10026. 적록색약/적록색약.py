def solve(arr):
    def bfs(si, sj):
        q = []

        q.append((si, sj))
        v[si][sj] = 1

        while q:
            ci, cj = q.pop(0)

            for di, dj in dir:
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj] == arr[ci][cj]:
                    v[ni][nj] = 1
                    q.append((ni, nj))

    v = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                bfs(i, j)
                cnt += 1
    return cnt


N = int(input())
pic = [list(map(str, input().strip())) for _ in range(N)]
fake = [[0]*N for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


for i in range(N):
    for j in range(N):
        if pic[i][j] == 'R' or pic[i][j] == 'G':  # 적녹은 0으로, 청은 1로 fake를 채움
            fake[i][j] = 0
        elif pic[i][j] == 'B':
            fake[i][j] = 1

ans = solve(pic)
ans_ = solve(fake)

print(ans, ans_)