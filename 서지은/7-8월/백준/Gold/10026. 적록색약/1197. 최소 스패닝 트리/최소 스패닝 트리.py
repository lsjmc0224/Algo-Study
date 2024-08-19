'''
간선을 가중치를 기준으로 오름차순 정렬
간선을 순차적으로 순회하며 최소 신장 트리를 만듦
서로소 집합 알고리즘에 기반, 트리에 순환성이 생기지 않는 간선만 추가
최소 신장 트리가 될 때까지 위 과정을 반복

'''

import os, io, sys

sys.setrecursionlimit(100000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def find(n):  # find 함수
    if n != parents[n]:
        parents[n] = find(parents[n])
    return parents[n]

def union(a, b):  # union 함수
    parents[find(b)] = find(a)


V, E = map(int, input().split())
parents = [n for n in range(V+1)]
adj = []
ans = 0

for _ in range(E):  # sorting해야 하므로 가중치를 가장 앞으로 넣어줌
    s, e, w = map(int, input().split())
    adj.append((w, s, e))

adj.sort()  # adj 오름차순 정렬

for w, s, e in adj:
    if find(s) != find(e):  # 만약 s와 e의 부모노드가 같지 않다면
        union(s, e)  # s와 e를 union 시켜준 뒤
        ans += w  # 최종 결과값이 가중치를 더해준다

print(ans)