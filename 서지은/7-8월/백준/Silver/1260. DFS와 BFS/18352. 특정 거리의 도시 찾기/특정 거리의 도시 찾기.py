'''
최단 거리가 정확히 K인 도시를 모두 출력
'''
from collections import deque
def solve(start, cnt):
    queue = deque()
    visited[start] = 1
    queue.append((start, cnt))

    while queue:
        cur, cnt = queue.popleft()

        if cnt == K:
            ans.append(cur)

        elif cnt < K:
            for n in adj[cur]:
                if visited[n] == 0:
                    visited[n] = 1
                    queue.append((n, cnt + 1))


N, M, K, X = map(int, input().split())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
ans = []

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)  # 단방향 도로

solve(X, 0)

if ans:
    ans.sort()
    print(*ans, sep=" ")
else:
    print(-1)