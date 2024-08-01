from collections import deque

def bfs():
    global cnt
    q = deque()

    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                q.append((i, j))  # def 안에서 for문 돌리고 이걸 바로 append
                v[i][j] = 1  # 이 점은 방문처리 해줌

    #  초기에 토마토 중에 0이 하나도 없으면
    if not any (tomato[i][j] == 0 for i in range(N) for j in range(M)):
        return 0 


    while q:
        ci, cj = q.popleft()

        for di, dj in dir:
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0 and tomato[ni][nj] == 0:
                v[ni][nj] = v[ci][cj] + 1
                q.append((ni, nj))
                cnt = max(cnt, v[ni][nj])

    for i in range(N):
        for j in range(M):  # 다 돌았는데도 방문한 적도 없고 익지도 않은 토마토가 있다? 토마토 익히기 실패!
            if tomato[i][j] == 0 and v[i][j] == 0:
                return -1

    return cnt-1  # 외엔 성공한 거니까 cnt-1값 리턴


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
v = [[0]*M for _ in range(N)]
cnt = 0

print(bfs())