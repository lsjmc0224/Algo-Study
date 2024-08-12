from collections import deque

def bfs(si, sj, h):
    q = deque()

    v[si][sj] = 1
    q.append((si, sj))

    global cnt

    while q:
        ci, cj = q.popleft()

        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and v[ni][nj] == 0 and arr[ni][nj] > h:
                v[ni][nj] = 1
                q.append((ni, nj))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
mx = max(map(max, arr))
res = []

for i in range(mx):
    cnt = 0
    v = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if arr[j][k] > i and v[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    res.append(cnt)

print(max(res))