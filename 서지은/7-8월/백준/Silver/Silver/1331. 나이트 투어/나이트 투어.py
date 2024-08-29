moves = list(input() for _ in range(36))
chess = []
# visited = [[0]*6 for _ in range(6)]
dir = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

is_valid = True
for n in moves:
    if moves.count(n) > 1:  # 같은 좌표가 2개 이상 들어있을 시
        is_valid = False
        break
    else:
        x, y = ord(n[0])-65, int(n[1])-1 # 입력받는 모든 체스판을 숫자형으로 변환 후 좌표로 넣어줌
        chess.append((x, y))

# 모든 좌표 값이 중복되지 않게 chess에 들어가있을 경우
# x, y가 이전의 시작점 중 ni, nj에 해당하는 지 여부 판단
if len(chess) == 36:

    step = 0

    for i in range(1, 36):
        x, y = chess[i]
        n, m = chess[i-1]

        flag = False

        for di, dj in dir:
            ni, nj = n+di, m+dj
            if 0<=ni<6 and 0<=nj<6:
                if (x, y) == (ni, nj):
                    is_valid = True
                    break
        else:
            is_valid = False
            break

    if is_valid == True:
        for i, j in dir:
            tp1, tp2 = chess[-1]
            tp1, tp2 = tp1+i, tp2+j
            s1, s2 = chess[0]

            if (tp1, tp2) == (s1, s2):
                is_valid = True
                break
            else: is_valid = False
            step += 1

if is_valid:
    print('Valid')
else: print('Invalid')

