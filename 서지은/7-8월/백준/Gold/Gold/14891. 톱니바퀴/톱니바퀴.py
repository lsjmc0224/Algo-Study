'''
구상)
계속해서 확인해야 하는 톱니바퀴의 idx는 2번과 8번 (3, 9에 해당)
각 톱니바퀴를 각각의 배열로 받은 뒤, 해당 인덱스에 해당하는 값이 얼마인지 확인

// 상극인지 동극인지를 확인하는 함수 -> 각 명령어에 따라 톱니바퀴 돌리는 함수
-> n번쨰 톱니바퀴를 반시계(-1) 혹은 시계 (1) 방향으로 돌리는 함수
    1. 1번 톱니바퀴는 2번째 인덱스만, 2, 3번은 2, 8번쨰, 4번은 8번째만 확인
    2. 입력받은 톱니바퀴 넘버를 기준으로, 1번에 들어있는 값에 따라
        같을 때만 톱니바퀴 돌리는 함수로 보내기
    2-1. 상극일 경우, 끝번의 톱니바퀴까지 전부 2, 8번 인덱스 확인
    2-2. 동극일 경우, 해당 순번에서는 아무 일도 일어나지 않음

    3. 결국 시계 방향이든, 반시계 방향이든 i+1방향으로 배열 속 값들을 움직이냐,
        i-1 방향으로 배열 속 값을 움직이냐의 차이

`   ** 결국 앞번의 idx == 2와 뒷번의 idx == 8을 비교
        -> 같으면 continue
        -> 다르면 배열 움직임을 반복
모든 함수가 다 돌아간 뒤, 각 톱니바퀴의 0번째 idx의 값을 확인해서 점수

1514 (1349) : 구현
1544 : 디버깅
... while문에서 자꾸 톱니들이 튕겨서 그냥 하드코딩했더니 됨.....
바야흐로 1646
..
마지막 테케가 틀리심 -> 디버거 사용
.. 해결 중 ...
마지막 테케만 걸리는 이유를 찾기
:

'''
def before_return(n, d):
    global fake_topni

    move_topni(n, d)
    for i in range(4):
        if fake_topni[i][0] != -1:
            topni[i] = fake_topni[i]


def move_topni(n, d):
    global fake_topni
    if d == -1:  # 반시계 방향으로 움직여야 할 때
        for j in range(7, -1, -1):
            if j-1 == -1:
                fake_topni[n][7] = topni[n][0]
            else:
                fake_topni[n][j-1] = topni[n][j]

    elif d == 1:  # 시계 방향으로 움직여야 할 때
        for j in range(8):
            if j+1 == 8:
                fake_topni[n][0] = topni[n][7]
            else:
                fake_topni[n][j+1] = topni[n][j]



def check_ns(n, d):  # 상극인지 동극인지 확인하는 함수
    global fake_topni

    if n == 0:  # 오른쪽 것만 체크
        if topni[n][2] == topni[n+1][6]:
            before_return(n, d)
            return
        else:
            move_topni(n, d)
            move_topni(n+1, -d)
            if topni[n+1][2] != topni[n+2][6]:
                move_topni(n+2, d)
                if topni[n+2][2] != topni[n+3][6]:
                    move_topni(n+3, -d)


    elif n == 1:  #  왼쪽일 때 오른쪽일 때 나눠야 됨!!!!!!!!!!!!!
        if topni[n-1][2] == topni[n][6] and topni[n][2] == topni[n+1][6]:  # 양쪽 다 같은 극일 때
            before_return(n, d)
            return
        else:
            move_topni(n, d)
            if topni[n-1][2] != topni[n][6]:  #왼쪽 톱니 먼저 탐색
                move_topni(n-1, -d)

            if topni[n][2] != topni[n+1][6]:  # 오른쪽 톱니 탐색
                move_topni(n+1, -d)
                if topni[n+1][2] != topni[n+2][6]:
                    move_topni(n+2, d)

    elif n == 2:
        if topni[n-1][2] == topni[n][6] and topni[n][2] == topni[n+1][6]:  # 양쪽 다 같은 극일 때
            before_return(n, d)
            return
        else:
            move_topni(n, d)
            if topni[n-1][2] != topni[n][6]:  #왼쪽 먼저 탐색
                move_topni(n-1, -d)
                if topni[n-1][6] != topni[n-2][2]:
                    move_topni(n-2, d)

            if topni[n][2] != topni[n+1][6]:  # 오른쪽 탐색
                move_topni(n+1, -d)

    elif n == 3:  # 마지막 톱니
        if topni[n][6] == topni[n-1][2]:
            before_return(n, d)
            return
        else:
            move_topni(n, d)
            move_topni(n-1, -d) # 왼쪽 톱니로 쭉 감
            if topni[n-1][6] != topni[n-2][2]:
                move_topni(n-2, d)

                if topni[n-2][6] != topni[n-3][2]:
                    move_topni(n-3, -d)


    for i in range(4):
        if fake_topni[i][0] != -1:
            topni[i] = fake_topni[i]



# 톱니바퀴 한 번에 받고 인덱스로 비교하기
topni = [list(map(int, input().strip())) for _ in range(4)]
K = int(input())

total = 0

for _ in range(K): # 임시로 저장할 톱니
    fake_topni = [[-1]*8 for _ in range(4)]
    num, dir = map(int, input().split())
    check_ns(num-1, dir)


if topni[0][0] == 1:
    total += 1
if topni[1][0] == 1:
    total += 2
if topni[2][0] == 1:
    total += 4
if topni[3][0] == 1:
    total += 8

print(total)