'''
1) 문제 이해
다도해의 지도는 R*C
X는 땅, .은 바다
50년이 지나면 인접한 세 칸 이상 바다가 있는 땅은 모두 잠김
// 사방 중 3칸 이상이 바다면 50년 뒤에 X가 .으로 변함
지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형
// min값으로 갱신, 아예 0이 되어 사라지진 않음

2) 구상
모두 x로 채워져 있는 가상의 지도 만들기
가상의 지도와 실제 지도를 비교하며, .인 부분은 넘어가고,
지도에서 땅인 X 값을 기준으로 bfs, (굳이 함수로 안 만들어도 될 듯)
만약 4방 탐색 중, cnt가 3번 이상이라면 (3면 이상이 .이라면)
50년 뒤에 바다에 잠기므로 탐색이 끝난 뒤 해당 좌표를 .으로 마킹

탐색이 끝난 뒤, X가 남아있는 곳을 기준으로 h, w값 잡고 해당 범위만큼
가상의 지도 결과로 출력

3)
1519 : 디버깅
// 섬만 남은 부분을 어떻게 잘라서 출력할 것인가?
X가 존재하는 i와 j의 max값을 찾아서 해당 범위 안에서만 jido 출력

1527 : 문제되는 부분)
두 번째 테스트케이스 좌측 하단 부분이 왜 사라져야 하는지 .. ?
1552:
지도의 가장 바깥 부분이 전부 바다라고 했으니 4면을 .으로 추가해줘야 함
나는 바보야

'''
from collections import  deque

def check_jido(si, sj):
    q = deque()
    q.append((si, sj))

    cnt = 0
    step = 0
    curSize = len(q)

    for _ in range(curSize):
        while q:
            ci, cj = q.popleft()

            for di, dj in dir:
                ni, nj = ci+di, cj+dj
                if not(0<=ni<R+2 and 0<=nj<C+2): continue
                if jido[ni][nj] == '.':  # 인접한 곳이 바다일 떄
                    cnt += 1

        if cnt >= 3:
            virtual[ci][cj] = '.'  # 3면 이상이 바다라면
            cnt = 0
        else:
            virtual[ci][cj] = 'X'  # 3면 이상이 바다가 아니라면 여전히 섬
            cnt = 0
    step += 1


R, C = map(int, input().split())
jido = ['.' * (C + 2)] + ['.' + input().strip() + '.' for _ in range(R)] + ['.' * (C + 2)]
virtual = [['.']*(C+2) for _ in range(R+2)]  # 가상의 지도 공란으로 채움
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(R+2):
    for j in range(C+2):
        if jido[i][j] == 'X':
            check_jido(i, j)

mini, minj = 11, 11
maxi, maxj = 0, 0
for i in range(R+2):
    for j in range(C+2):
        if virtual[i][j] == 'X':
            mini = min(mini, i)
            minj = min(minj, j)
            maxi = max(maxi, i)
            maxj = max(maxj, j)

for i in range(mini, maxi+1):
    for j in range(minj, maxj+1):
        print(virtual[i][j], end="")
    print(end='\n')