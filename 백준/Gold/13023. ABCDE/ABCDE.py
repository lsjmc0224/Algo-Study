# 참가자는 N명, 번호는 0 ~ N-1번
# 연결된 모든 가짓 수를 다 확인해야 하므로 백트래킹 이용
# n은 선택된 친구 수

def dfs(n, start):
    global ans

    if ans == 1:
        return

    if n == 5:
        ans = 1
        return

    for end in adj[start]:
        if visited[end] == 0:
            visited[end] = 1
            dfs(n+1, end)
            visited[end] = 0


N, M = map(int, input().split())
adj =[[] for _ in range(N+1)]
visited = [0]*N
ans = 0

for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for start in range(N):  # 0부터 방문표시 해준 뒤 dfs를 1부터 돌림
    visited[start] = 1
    dfs(1, start)
    visited[start] = 0  # 다녀온 뒤에는 다시 0으로 처리해줌

print(ans)