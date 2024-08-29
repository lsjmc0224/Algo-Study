def check_move(com, n):
    global si, sj, direction

    if com == 'MOVE':
        if direction == 1:  # 동쪽을 보고 있을 때
            si += d
        elif direction == 2:  # 서쪽을 보고 있을 때
            si -= d
        elif direction == 3:  # 남쪽을 보고 있을 때
            sj -= d
        elif direction == 4:  # 북쪽을 보고 있을 때
            sj += d

        if not (0 <= si <= M and 0 <= sj <= M):
            return -1

    elif com == 'TURN':
        if d == 0:  # 현재 위치에서 왼쪽으로 90도 회전
            if direction == 1:  # 기존 위치가 동쪽일 때
                direction = 4
            elif direction == 2:  # 기존 위치가 서쪽일 때
                direction = 3
            elif direction == 3:  # 기존 위치가 남쪽일 때
                direction = 1
            elif direction == 4:  # 기존 위치가 북쪽일 때
                direction = 2

        elif d == 1:  # 현재 위치에서 오른쪽으로 90도 회전
            if direction == 1:
                direction = 3
            elif direction == 2:
                direction = 4
            elif direction == 3:
                direction = 2
            elif direction == 4:
                direction = 1
    return 0


M, N = map(int, input().split())
si, sj = 0, 0
direction = 1
ans = 0
# 동 1 서 2 남 3 북 4

for _ in range(N):
    command, d = input().split()
    d = int(d)
    ans = check_move(command, d)

    if ans == -1:
        print(-1)
        break
else:
    print(si, sj)