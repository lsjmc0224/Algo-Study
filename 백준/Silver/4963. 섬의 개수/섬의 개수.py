# 땅은 1, 바다는 0, 종료 조건은 0 0 입력 시
# 팔방 탐색하여 1이 연결 되어 있으면 섬 하나로 침 (cnt += 1)
from collections import deque


def bfs(si, sj):
    queue = deque()

    visited[si][sj] = 1
    queue.append((si, sj))

    while queue:
        ci, cj = queue.popleft()
        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and visited[ni][nj] == 0 and jido[ni][nj] == 1:
                visited[ni][nj] = 1
                queue.append((ni, nj))


while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:  # 계속해서 돌다가 0 0 이 입력되었을 때 종료 // W H 와 크기가 같으니
        break

    jido = [list(map(int, input().split())) for _ in range(H)]
    dir = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # 팔방 탐색
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    
    for i in range(H):
        for j in range(W):
            if visited[i][j]==0 and jido[i][j] == 1:  # 방문한 적 없고, 1일 때 bfs 탐색
                bfs(i, j)
                cnt += 1  # 다 돌고 나왔을 때 섬을 하나로 치기 때문에 += 1

    print(cnt)