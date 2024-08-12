# bfs로 최단인 거리를 탐색, 케빈 베이컨의 수가 가장 작은 사람, 다수일 시 번호가 더 작은 사람 출력
# 사람의 번호는 1번 ~ N번
from collections import deque


def bfs(start):

    queue = deque()
    visited[start] = 1
    queue.append(start)

    while queue:
        c = queue.popleft()
        for n in adj[c]:
            if visited[n] == 0:
                visited[n] = visited[c] + 1
                queue.append(n)


N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]  # 사람과 친구 관계를 담을 adj 배열
ans = []

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)  # 양방향으로 adj 배열에 넣어줌

for i in range(1, N+1):
    visited = [0] * (N + 1)  # visited는 bfs 돌 때마다 초기화 해줘야 하니까 ... ㅠㅠ
    bfs(i)  # 1부터 N까지 돎
    ans.append(sum(visited))  # visited에 기록된 합계를 ans에 append 해줌

print(ans.index(min(ans))+1)  # ans의 최소 인덱스를 찾고 거기에 +1 해줌