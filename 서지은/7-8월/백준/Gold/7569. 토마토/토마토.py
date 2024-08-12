from collections import deque
import sys

input = sys.stdin.read
def bfs():
    queue = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]
    cnt = 0

    for k in range(H):
        for i in range(N):
            for j in range(M):
                if tomato[k][i][j] == 1:
                    visited[k][i][j] = 1
                    queue.append((k, i, j))
                elif tomato[k][i][j] == 0:
                    cnt += 1

    if cnt == 0:  # 안 익은 토마토가 없으면 0 리턴
        return 0


    while queue:
        ch, ci, cj = queue.popleft()

        for dh, di, dj in dir:
            nh, ni, nj = ch+dh, ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and 0<=nh<H and visited[nh][ni][nj] == 0 and tomato[nh][ni][nj] == 0:
                visited[nh][ni][nj] = visited[ch][ci][cj] + 1
                queue.append((nh, ni, nj))
                cnt -= 1

    if cnt > 0:
        return -1
    else:
        return visited[ch][ci][cj] - 1


data = input().split()

M, N, H = int(data[0]), int(data[1]), int(data[2])
index = 3
tomato = [[[int(data[index + k + j * M + i * N * M]) for k in range(M)] for j in range(N)] for i in range(H)]


dir = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, 1), (0, 0, -1)]

print(bfs())