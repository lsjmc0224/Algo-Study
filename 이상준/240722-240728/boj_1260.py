# DFS와 BFS (https://www.acmicpc.net/problem/1260)

# 정점의 개수 = N, 간선의 개수 = m
n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for i in range( n + 1 )]

# 그래프 받기
for i in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

# DFS
def dfs(curr_node):
    print(curr_node, end = ' ')
    visited[curr_node] = 1
    for i in range(1, n + 1):
        if graph[curr_node][i] == 1 and not visited[i]:
            dfs(i)


# BFS()
def bfs(start_node):
    queue = [start_node]
    visited[start_node] = 1
    while queue:
        curr_node = queue.pop(0)
        print(curr_node, end = ' ')
        for i in range(1, n + 1):
            if graph[curr_node][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
visited = [0] * (n + 1)
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)


