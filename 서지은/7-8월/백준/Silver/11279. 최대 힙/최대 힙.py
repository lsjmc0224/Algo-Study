import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    tmp = int(input())

    if tmp != 0:
        heapq.heappush(heap, (-tmp, tmp))
    else:
        if heap:
            mx_item = heapq.heappop(heap)[1]
            print(mx_item)
        else:
            print(0)