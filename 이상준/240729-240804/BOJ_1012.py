# 유기농 배추 ( https://www.acmicpc.net/problem/1012 )
# 테스트케이스T, 행N, 열M, 배추개수K

# 그리드 가져와
# visited 가져와
# count = 0
# 각점에 대해 grid가 1이고 visited가0이고 갈수 있다면 bfs ㄱㄱ
# count += 1

def bfs(start_row, start_col):
    queue = [(start_row, start_col)]
    visited[start_row][start_col]
    while queue:
        curr_node = queue.pop()
        x, y = curr_node[0], curr_node[1]
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = 1

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
t = int(input())
for i in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    grid = [[0] * m for i in range(n)]
    for i in range(k):
        row, col = map(int, input().split())
        grid[row][col] = 1
    visited = [[0] * m for i in range(n)]

    for row in range(n):
        for col in range(m):
            if grid[row][col] == 1 and visited[row][col] == 0:
                bfs(row, col)
                cnt +=1

    print(cnt)