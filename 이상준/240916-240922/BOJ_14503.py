# 로봇 청소기 https://www.acmicpc.net/problem/14503

# 방크기 n, m
n, m = 3, 3

# 로봇청소기 위치 r, c
# 로봇청소기 방향 d
r, c, d = 1, 1, 0

# 청소한 칸의 수
cnt = 0

# 청소한 칸 기록 grid
cleaned_grid = [[0 for _ in range(m)] for _ in range(n)]
print(cleaned_grid)
# 방의 구조 grid 
room_grid = [list(map(int, input().split())) for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
# 로봇 청소 후 이동
if cleaned_grid[r][c] == 0:
    cleaned_grid[r][c] = 1

# 로봇 주변 4칸 중 청소되지 않은 빈칸이 없는 경우
def is_everywhere_clean(r, c):
    for i in range(4):
        nxt_r = r + dxs[i]
        nxt_c = r + dys[i]
        if 0 <= nxt_r <= (n - 1) and 0 <= nxt_c <= (n - 1) 
            if cleaned_grid[nxt_r][nxt_c] == 0 and room_grid[nxt_r][nxt_c] == 0:
                return 0
    else:
        return 1

if is_everywhere_clean(r, c)
while 1:
    d = (d - 1) % 4
    nxt_r = r + dxs[d]
    nxt_c = c + dys[d]
    # 돌다가 더러우면 다음칸으로 이동
    if cleaned_grid[nxt_r][nxt_c] == 0:
        r = nxt_r
        c = nxt_c
        break

