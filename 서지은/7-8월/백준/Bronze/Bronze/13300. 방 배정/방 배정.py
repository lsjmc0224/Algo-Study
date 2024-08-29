N, K = map(int, input().split())

w_lst = []
m_lst = []
for _ in range(N):
    S, Y = map(int, input().split())
    if S == 0:
        w_lst.append(Y)
    else:
        m_lst.append(Y)

cnt = 0
for i in range(1, 7):
    num1 = w_lst.count(i)
    num2 = m_lst.count(i)

    if num1 > K:
        while num1 > K:
            num1 -= K
            cnt += 1
        cnt += 1
    elif 0 < num1 <= K:
        cnt += 1

    if num2 > K:
        while num2 > K:
            num2 -= K
            cnt += 1
        cnt += 1
    elif 0 < num2 <= K:
        cnt += 1

print(cnt)