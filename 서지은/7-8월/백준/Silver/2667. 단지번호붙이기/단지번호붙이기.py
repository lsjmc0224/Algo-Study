# 2차원 배열 bfs 사방탐색
# 1인 부분들 중 i, j가 최소인 점을 시작 지점으로 queue에 넣은 뒤
# 1일 때만 (range 범위 제한 시 작성) bfs 진행
# 바깥에 cnt 올려준 뒤 하나의 bfs가 끝났을 때마다 ans.append, 이후 ans.sort()
# cnt를 하나씩 올려준 뒤 cnt만큼 for문을 돌려서 i의 갯수를 세준다

from collections import deque

def bfs(si, sj):
    global cnt
    queue = deque()

    visited[si][sj] = cnt
    queue.append((si, sj))

    while queue:
        ci, cj = queue.popleft()

        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and village[ni][nj] == 1:
                visited[ni][nj] = cnt
                queue.append((ni, nj))


N = int(input())
village = [list(map(int, input().strip())) for _ in range(N)]
ans = []
visited = [[0]*N for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
cnt = 1

for i in range(N):
    for j in range(N):
        if village[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

visited_1 = sum(visited, [])
for i in range(1, cnt):
    temp = visited_1.count(i)
    ans.append(temp)

ans.sort()
print(cnt-1)
for n in ans:
    print(n)