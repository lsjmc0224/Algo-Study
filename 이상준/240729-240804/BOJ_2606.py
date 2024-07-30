# 바이러스 ( https://www.acmicpc.net/problem/2606 )
# 인접 행렬 받아와
# bfs (만약 이 노드에 연결된 노드가 있으면 계속 append, queue.pop(0)

n = int(input()); m = int(input())
grid = [[0]*(n+1) for i in range(n+1)]
for i in range(m):
    start, end = map(int, input().split())
    grid[start][end] = 1
    grid[end][start] = 1
visited = [0] * (n + 1)

def bfs(start_node):
    virus_cnt = 0
    queue = [start_node]
    visited[start_node] = 1
    while queue:
        curr = queue.pop(0)
        for i in range(1, n+1):
            if grid[curr][i] == 1 and not visited[i]:
                queue.append(i)
                virus_cnt += 1
                visited[i] = 1
    return virus_cnt
print(bfs(1))