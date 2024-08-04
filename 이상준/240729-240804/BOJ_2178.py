# grid 받아와
# visited 받아와

n, m = map(int, input().split())
grid = [list(map(int, list(input()))) for i in range(n)]
visited = [[0] * m for i in range(n)]

# bfs

dxs = [0,1,0,-1]
dys = [1,0,-1,0]
def bfs(ix, iy):
    cnt = 1
    queue = [(ix,iy)]
    visited[ix][iy] = 1
    while queue:
        curr = queue.pop(0)
        x = curr[0]
        y = curr[1]
        for i in range(4):
            nx = x + dxs[i]
            ny = y + dys[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
bfs(0,0)
print(visited[n-1][m-1])