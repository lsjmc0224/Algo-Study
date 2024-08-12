# 넓이인 area랑 cnt 올리는 데에 에러가 있는 듯
# 아침에 출근해서 트러블 슈팅 하세요 ~ 🩷

import sys
sys.setrecursionlimit(10000)

def dfs(si, sj):
    v[si][sj] = 1
    global area  # 전역 변수 선언
    area += 1  # area에 각 0 범위 탐색 후 0 갯수만큼 += 1

    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = si+di, sj+dj
        if 0<=ni<M and 0<=nj<N and v[ni][nj] == 0 and paper[ni][nj] == 0:
            dfs(ni, nj)
    return area


M, N, K = map(int, input().split())
paper = [[0]*N for _ in range(M)]
v = [[0]*N for _n in range(M)]
cnt = 0
ans = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):  # paper에 칠해진 부분 1 더해주기
        for j in range(x1, x2):
            paper[i][j] += 1  # 종이 범위 중 i가 반대로 제시되어 있기 때문에 j, i 로 넣어줌

for i in range(M):
    for j in range(N):
        # 아무 것도 칠해지지 않은 부분을 기준으로 dfs
        if paper[i][j] == 0 and v[i][j] == 0:
                    area = 0 # dfs 호출 전 초기화를 시켜줘야 함
                    dfs(i, j)
                    cnt += 1
                    ans.append(area)
ans.sort()
print(cnt)
print(*ans)