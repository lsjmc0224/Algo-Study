from collections import deque

# BFS를 활용해 하루 단위로 익음을 전파
def bfs(grid, rows, cols):
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # 익은 토마토의 위치를 큐에 추가
                queue.append((row, col))

    days = -1
    drs = [0, 0, 1, -1]
    dcs = [1, -1, 0, 0]

    while queue:
        for _ in range(len(queue)):  # 현재 큐에 있는 모든 위치를 처리
            row, col = queue.popleft()
            for i in range(4):
                nxt_row, nxt_col = row + drs[i], col + dcs[i]
                if 0 <= nxt_row < rows and 0 <= nxt_col < cols and grid[nxt_row][nxt_col] == 0:
                    grid[nxt_row][nxt_col] = 1
                    queue.append((nxt_row, nxt_col))
        days += 1

    # 익지 않은 토마토가 남아있는지 확인
    for row in grid:
        if 0 in row:
            return -1
    return days


# 입력 처리
cols, rows = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(rows)]

# BFS 실행 및 결과 출력
result = bfs(grid, rows, cols)
print(result)
