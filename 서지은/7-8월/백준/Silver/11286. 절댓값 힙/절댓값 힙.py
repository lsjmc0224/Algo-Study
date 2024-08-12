import heapq, sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    tmp = int(input())

    if tmp != 0:
        heapq.heappush(heap, (abs(tmp), tmp))
    else:
        if heap:
            item = heapq.heappop(heap)[1]
            print(item)
        else:
            print(0)