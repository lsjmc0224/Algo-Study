# 입력받은 뒤, 행 / 열 / 대각선을 돌며 5일 떄 (=빙고일 때) yaho += 1 해주는 함수
# 빙고판과 사회자가 불러주는 것 모두 2차원 배열로 입력받음
# arr를 돌면서 arr[i][j]위치에 n이 있으면 cnt를 올려줌

def check_bingo():
    yaho = 0

    # 행 체크
    for row in bingo:
        if sum(row) == 5:
            yaho += 1
    # 열 체크
    for col in zip(*bingo):
        if sum(col) == 5:
            yaho += 1
    # 대각선 체크
    if sum(bingo[i][i] for i in range(5)) == 5:  # \ 이 모양
        yaho += 1
    if sum(bingo[i][4-i] for i in range(5)) == 5:  # / 이 모양
        yaho += 1

    return yaho

arr = [list(map(int, input().split())) for _ in range(5)]
bingo = [[0]*5 for _ in range(5)]
num = [list(map(int, input().split())) for _ in range(5)]
nums = sum(num, [])

cnt = 0

for n in nums:
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                bingo[i][j] = 1
                cnt += 1
                if cnt >= 5:
                    yaho = check_bingo()
                    if yaho >= 3:
                        print(cnt)
                        exit()