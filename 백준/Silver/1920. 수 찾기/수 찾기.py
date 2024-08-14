# lst_m안의 수들이 lst_n안에 존재하는 지
# 비교 대상은 lst_n, while문으로 돌리면서 s <= e일 때까지
# s1, e1은 lst_n의 idx / s2, e2는 lst_m의 idx

N = int(input())
lst_n = list(map(int, input().split()))
lst_n.sort()
M = int(input())
lst_m = list(map(int, input().split()))

s = ans = 0
e = N-1

for n in lst_m:
    s = ans = 0
    e = N - 1
    while s <= e:
        m = (s+e) // 2

        if lst_n[m] == n:
            ans = 1
            break
        elif lst_n[m] < n:
            s = m + 1
        else:
            e = m - 1

    print(ans)