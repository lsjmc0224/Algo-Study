'''
초기에 n+1개의 집합 {0} ... {n}
합집합 연산과 두 원소가 같은 집합 포함 여부
집합을 표현하는 프로그램

m은 연산의 개수
앞이 0이 올 경우 합집합 연산을 진행,
1이 올 경우, a와 b가 같은 집합에 포함되어 있는지를 확인해서 출력 // 이 떄만 출력함
'''

import os, io, sys

sys.setrecursionlimit(100000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def find(z):
    if z != parents[z]:
        parents[z] = find(parents[z])
    return parents[z]


def union(x, y):
    parents[find(y)] = find(x)


N, M = map(int, input().split())
parents = [n for n in range(N+1)]  # N+1개의 부모 리스트

for _ in range(M):
    check, a, b = map(int, input().split())

    if check == 0:  # 합집합 연산을 해줘야 할 때
        union(a, b)  # check에 0이 들어올 떄 a와 b를 합집합 연산해줘야 함

    else:  # check에 1이 들어와 있을 때, a와 b가 같은 집합에 포함 시 yes / 아니면 no 출력
        if find(a) == find(b): print('YES')
        else: print('NO')

