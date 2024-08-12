# K개의 글자로만 이루어진 단어만을 읽을 수 있음
# 언어의 모든 단어는 anta로 시작 // tica로 끝남 // 단어는 N개
# N <= 50, 자연수  // 0 <= K <= 26, 자연수
# 단어는 영어 소문자 구성, 길이는 8~15 // 모든 단어는 중복되지 않음
# ----------------------------------------------------
# a n t i c 는 무조건 .. 뭔갈 하고 K-5 만큼 더 가르칠 수 있음 / 근데 K가 5보다 작아버리면 0 리턴
# 남은 알파벳들 중에 K-5개만큼 조합 만들어서 몇 개의 단어를 읽을 수 있는지 카운트
# dfs 돌리는 건 K-5개만큼 가능한 조합의 경우를 만들어서 체크하는 거고 바깥에다가 입력받은 단어들하고 대입하는 로직


def dfs(n, lst, start, length):
    global max_words

    if len(lst) == length:
        cnt = 0
        teach_letters = essential.union(lst)  # 가르친 단어들에 antic이랑 조합이랑 합친 걸 넣어줌
        # num = count_words(words, teach_letters)  # 입력받은 단어들이랑 위에 합쳐준 애들로 단어 몇 개 읽을 수 있는지 함수로 확인

        for word in words:
            readable = True
            for n in word:
                if n not in teach_letters:
                    readable = False
                    break
            if readable:
                cnt += 1

        max_words = max(max_words, cnt)  # 최댓값을 구해줌 // 각 조합 별로 읽을 수 있는 단어의 갯수가 다 달라지니
        return

    for i in range(start, len(n)):
        lst.add(n[i])  # 빈 리스트에다가 reamins[0]번부터 추가함
        dfs(n, lst, i+1, length)  # 조합으로 짜야 해서 start지점을 i+1로 잡아줌
        lst.remove(n[i])


# def count_words(words, teach_letters):
#     cnt = 0
#     for word in words:
#         if all (n in teach_letters for n in word):  # teach_letter에 있는 단어들이 word에 모두 있다면
#             cnt += 1  # 그 단어는 읽을 수 있는 단어이므로 cnt += 1
#     return cnt


N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]
essential = {'a', 'n', 't', 'i', 'c'}  # 필수로 가르쳐야 하는 알파벳
remains = list(set('bdefghjklmopqrsuvwxyz'))  # 필수를 뺀 남은 알파벳들 // list(set()) 민협님 코드에서 훔쳐옴
max_words = 0

if K < 5:
    print(0)
else:
    mx_len = K-5  # 최대로 가르칠 수 있는 글자는 K-5
    combs = []
    dfs(remains, set(), 0, mx_len)
    print(max_words)