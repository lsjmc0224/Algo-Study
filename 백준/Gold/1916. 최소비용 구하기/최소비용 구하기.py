import heapq

def dijk(s, e):
    heap = []
    D = [INF] * (N+1)  # 다익스트라 배열 최댓값으로 초기화

    heapq.heappush(heap, (0, s))
    D[s] = 0

    while heap:
        w, cur = heapq.heappop(heap)
        if D[cur] < w: continue

        for next, w in adj[cur]:
            if D[next] > D[cur] + w:
                D[next] = D[cur] + w
                heapq.heappush(heap, (D[next], next))
    return D[e]


INF = 1000 * 100000
N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))  # 단방향, 가중치와 함께 넣어줌

S, G = map(int, input().split())  # 출발점과 도착점의 도시 번호
ans = dijk(S, G)
print(ans)