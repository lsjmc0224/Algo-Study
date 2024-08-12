# 3개의 연속된 문제의 답은 같지 않다
# 5점 이상일 경우의 수
# level은 depth, cnt는 맞은 갯수, 빈 배열에 3개씩 넣어서 비교, res는 ~ 일 때의 경우의 수

def dfs(n, cnt, lst):
    global res

    if n == 10:
        if cnt >= 5:
            # is_flag = True
            # for i in range(2, 10):
            #     if lst[i] == lst[i-1] == lst[i-2]:
            #         is_flag = False
            #         break
            # if is_flag:
            res += 1
        return

    for i in range(1, 6):

        if n >= 2 and i==lst[n-1]==lst[n-2]:
            continue  # 다시 위로 올라가서 i+1의 동작을 수행하게 함

        lst.append(i)

        if i == answer[n]:
            dfs(n+1, cnt+1, lst)

        else:
            dfs(n+1, cnt, lst)

        lst.pop()


answer = list(map(int, input().split()))
res = 0


dfs(0, 0, [])
print(res)