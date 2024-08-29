'''
구상)
주어지는 카드의 장 수는 9장,
이 9장으로 만들 수 있는 모든 합의 경우가 필요
-> 가능한 순열을 어떻게 만들 수 있는지?
-> 각각의 속성들이 모두 같거나, 모두 다른 경우 // 전체에서 따지면 수가 너무 많아지므로
-> 2차원 배열 느낌으로 입력받고, [0][0], [1][0], [2][0]... 이런 식으로 비교하며
합이 가능한 경우인지를 검증하는 순열 로직 필요
=> 조건 모두 통과시 합이 가능한 카드들에 해당하므로, 해당 카드들의 i 인덱스를
튜플 형식으로 possible_lst에 append  (1, 3, 6) ...

한 줄의 입력마다 [0] [1] [2]를 매핑해서 각 구분 별로 리스트를 나누고,
리스트 인덱스는 입력받은 값에서 -1 해주거나 리스트 자체를 len == 10 배열로 선언

n줄에 걸쳐서 나오는 플레이어의 합 or 결을 각각 검증할 함수 필요
H가 들어왔을 시, H 검증 함수로 이동
-> 각 세 장을, 각각의 리스트에서 같은 인덱스로 데려와서 대조 비교
-> 각 리스트마다 모두 같거나 / 모두 다른지 여부 검증
-> 입력 받은 인덱스를 튜플 형식으로 ans_lst에 저장 후, 이미 append 돼 있는 지 동시 확인
 => 만약 둘 중 하나라도 안 되면 -1 후 return, 둘 다 해당하면 +3

G가 들어왔을 시, G 검증 함수로 이동
-> ans_lst에 들어있는 튜플의 갯수가 미리 가능한 조합을 만들어둔 lst와 len 비교
    => 만약 같지 않다면 모든 합이 나오지 않은 것이므로 -1 후 return

-> g_cnt 를 만들어서(global 선언) 만약 ans_lst와 possible_lst의 길이가 일치했을 때,
g_cnt += 1을 해주고 / 이 g_cnt == 1 이면 처음 외친 것이므로 +3
 => 만약 g_cnt가 > 1이라면 이전에도 G를 외침으로서 점수를 받아간 것이므로
    -1 후 return

최종 점수 출력
'''

# 합이 가능한지 체크하는 함수
def possible_check(a, b, c):
    s_flag = False
    sc_flag = False
    bg_flag = False

    if (shape[a] == shape[b] == shape[c]) or (shape[a]!=shape[b] and shape[b]!=shape[c] and shape[a]!=shape[c]):
        s_flag = True
    if (shape_color[a] == shape_color[b] == shape_color[c]) or (shape_color[a]!=shape_color[b] and shape_color[b]!=shape_color[c] and shape_color[a]!=shape_color[c]):
        sc_flag = True
    if (bg_color[a] == bg_color[b] == bg_color[c]) or (bg_color[a]!=bg_color[b] and bg_color[b]!=bg_color[c] and bg_color[a]!=bg_color[c]):
        bg_flag = True

    if s_flag == sc_flag == bg_flag == True:
        possible_lst.append((a, b, c))
    return


# 합 체크 함수
def check_H(a, b, c):
    global total
    # 각각 세 개의 요소가 모두 같은지 / 틀린지를 확인하기 위한 함수
    # 가능한지 확인하는 경우를 possible_lst에 넣었으니 그 요소와 비교

    # 여기서 체크할 때, abc 순서가 아니라 acb 순서여도 가능함
    possible = False
    for i, j, k in possible_lst:
        if a == i:
            if (b == j and c == k) or (b == k and c == j):
                possible = True
                break
        elif a == j:
            if (b == i and c == k) or (b == k and c == i):
                possible = True
                break
        elif a == k:
            if (b == i and c == j) or (b == j and c == i):
                possible = True
                break
        else: continue


    # 여기서 a, b, c in ans_lst를 검증할 때 순서에 걸리지 않아서
    # 아래 else로 넘어가는 이슈


    if possible:  # 합이 가능한 카드들일 때
        temp = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]
        for tp in range(6):  # 합을 외친 경우
            if temp[tp] in ans_lst:
                total -= 1
                break
        else:  # 합을 외치지 않았던 카드라면
            ans_lst.append((a, b, c))
            total += 1
            return

    else:  # 합이 불가능한 카드들일 경우
        total -= 1
        return

# 결 체크 함수
def check_G():
    global g_cnt, total

    if len(ans_lst) != len(possible_lst):
        total -= 1
        return
    else:
        g_cnt += 1
        if g_cnt == 1:  # 만약 이번이 G를 처음 외친 거라면
            total += 3
            return
        else:  # 만약 이전에도 가능한 G를 외친 적이 있다면
            total -= 1
            return

# 입력받은 카드에 대한 속성을 각각 담을 배열 선언 // 1부터 시작하므로
shape = [[] for _ in range(10)]
shape_color = [[] for _ in range(10)]
bg_color = [[] for _ in range(10)]

for i in range(9):
    sh, sh_co, bg_co = input().split()
    shape[i+1].append(sh)
    shape_color[i+1].append(sh_co)
    bg_color[i+1].append(bg_co)

possible_lst = []  # 합이 가능한 경우를 담을 빈 리스트

for i in range(1, 10):
    for j in range(i + 1, 10):
        for k in range(j + 1, 10):
            possible_check(i, j, k)  # '합'이 가능한 카드 조합인지 확인

N = int(input())

ans_lst = []  # 합을 외치고, 합이 맞았을 때의 경우를 담을 리스트
g_cnt = 0  # G 성공 횟수
total = 0  # 총 점수
for _ in range(N):
    shout = list(input().split())
    if shout[0] == 'H':
        one, two, three = int(shout[1]), int(shout[2]), int(shout[3])
        check_H(one, two, three)
    else:
        check_G()

print(total)