'''
고려사항)
처음 주어진 손가락의 위치가 단어의 시작점이 아닐 수 있음
sl/sr 에서 left_word / right_word로의 이동 거리 + 1
** 모든 키보드는 한 글자를 누를 때마다 시간이 1이 들어감

각 키를 누르는 시간 구하는 로직
// 각 키의 좌표값과 해당하는 글자를 dict 형태로 선언
// 쪼개어 입력받은 전체 단어를 한 글자씩 돌면서 l, r 판단
// 이후 각 상황에 따라 dict value에서 좌표값 꺼내오고,
// left or right의 좌표와 abs 연산
// 해당 값을 전체 sm에 더해줌

'''

sl, sr = input().split()
word = list(input())
keyboard = {'q':('l', 0, 0),
             'w':('l', 0, 1),
             'e':('l', 0, 2),
             'r':('l', 0, 3),
             't':('l', 0, 4),
             'a':('l', 1, 0),
             's':('l', 1, 1),
             'd':('l', 1, 2),
             'f':('l', 1, 3),
             'g':('l', 1, 4),
             'z':('l', 2, 0),
             'x':('l', 2, 1),
             'c':('l', 2, 2),
             'v':('l', 2, 3),
             'y':('r', 0, 5),
             'u':('r', 0, 6),
             'i':('r', 0, 7),
             'o':('r', 0, 8),
             'p':('r', 0, 9),
             'h':('r', 1, 5),
             'j':('r', 1, 6),
             'k':('r', 1, 7),
             'l':('r', 1, 8),
             'b':('r', 2, 4),
             'n':('r', 2, 5),
             'm':('r', 2, 6)}

# 입력받은 글자를 한 글자씩 돌면서
cnt = 0
for n in word:
    if keyboard[n][0] == 'l':  # 왼손의 범위일 때
        cnt += (abs(keyboard[n][1] - keyboard[sl][1]) + abs(keyboard[n][2] - keyboard[sl][2]))
        cnt += 1
        sl = n
    elif keyboard[n][0] == 'r':  # 오른손의 범위일 때
        cnt += (abs(keyboard[n][1] - keyboard[sr][1]) + abs(keyboard[n][2] - keyboard[sr][2]))
        cnt += 1
        sr = n
print(cnt)