from collections import deque

def bfs(s):
    q = deque()

    visited[s] = 1
    q.append(s)

    while q:
        c = q.popleft()
        for n in adj[c]:
            if visited[n] == 0:
                visited[n] = c  # 현재 c에서 인접한 n에 c값을 넣어줘야 부모 노드를 찾을 수 있음
                q.append(n)


N = int(input())
adj = [[] for _ in range(N+1)]

for i in range(N-1):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

visited = [0]*(N+1)
bfs(1)
print(*visited[2:], sep="\n")