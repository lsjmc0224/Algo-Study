'''
3184 양
.은 빈 필드, #는 울타리, o는 양, v는 늑대
울타리를 지나지 않고 다른 칸으로 이동이 가능하다면 두 칸은 같은 영역 안에 속해 있음
영역 얀의 양의 수 > 늑대의 수 : 이김, 늑대 쫓아냄
영역 안의 양의 수 < 늑대의 수 : 양 다 잡아먹힘
아침에 살아남은 양과 늑대는?

디버깅) cnt 세는 로직까지 도달이 안 돼서 여기 위치를 수정해줘야 함
sm += 하는 부분도
'''
from collections import deque
def bfs(si, sj):
    global v_cnt, o_cnt

    q = deque()
    visited[si][sj] = 1
    q.append((si, sj))

    step = 0
    curSize = 0

    while q:
        curSize = len(q)
        for _ in range(curSize):
            ci, cj = q.popleft()

            if field[ci][cj] == 'o':
                o_cnt += 1
            elif field[ci][cj] == 'v':
                v_cnt += 1

            for di, dj in dir:
                ni, nj = ci+di, cj+dj
                if not (0<=ni<R and 0<=nj<C): continue
                if visited[ni][nj] == 1: continue
                if field[ni][nj] == '#': continue
                visited[ni][nj] = 1
                q.append((ni, nj))

        step += 1
    return None


R, C = map(int, input().split())
field = [list(map(str, input().strip())) for _ in range(R)]
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[0]*C for _ in range(R)]
o_sm = v_sm = 0

for i in range(R):
    for j in range(C):
        if visited[i][j]==0 and field[i][j] in ('o', 'v'):
            o_cnt = v_cnt = 0
            bfs(i, j)
            if o_cnt > v_cnt:
                o_sm += o_cnt
            else: v_sm += v_cnt

print(o_sm, v_sm)