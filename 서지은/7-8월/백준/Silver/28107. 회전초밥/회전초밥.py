import heapq

heap = [[] for _ in range(200_001)]
N, M = map(int, input().split())

for i in range(1, N+1):
    lst = list(map(int, input().split()))
    for n in lst[1:]:  # k는 버림
        heapq.heappush(heap[n], i)  # 1번부터 heap[n]번째에 i(고객 번호)를 넣어줌

tlst = list(map(int, input().split()))  # 생성한 메뉴 번호를 받아줌
cnts = [0]*(N+1)
for menu in tlst:
    if heap[menu]:  # 메뉴가 heap에 있다면
        cnts[heap[menu].pop(0)] += 1  # 메뉴별 hqpop 해서 cnts[] 갯수 카운트

print(*cnts[1:])
