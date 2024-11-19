# https://www.acmicpc.net/problem/1952

# m, n 받아오기
m, n = map(int, input().split())

# visited grid 만들기
visited_grid = [ [0 for _ in range(n)] for _ in range(m) ]

# 시작 위치 방향 초기화
start_row = 0
start_col = 0
start_dir = 0
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]
count = 0

# 달팽이 이동
while 1:
    visited_grid[start_row][start_col] = 1
    nxt_row = start_row + drs[start_dir]
    nxt_col = start_col + dcs[start_dir]
    if 0 <= nxt_row < m and 0 <= nxt_col < n and not visited_grid[nxt_row][nxt_col]:
        start_row = nxt_row
        start_col = nxt_col
        continue
    # 길이없다
    else:
        # 꺾기
        start_dir = ( start_dir + 1 ) % 4

        # 꺾고보니 갔던 길임
        if visited_grid[start_row + drs[start_dir]][start_col + dcs[start_dir]]:
            break
        # 꺾고보니 갔던 길 아님
        else:
            count += 1
            start_row = start_row + drs[start_dir]
            start_col = start_col + dcs[start_dir]

print(count)
