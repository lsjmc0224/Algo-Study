N = int(input())
q_lst = [int(input()) for _ in range(N)]

def quickSort(lst):
    if len(lst) <= 1:
        return lst  # 그냥 끝내는 게 아니라 정렬한 lst를 보내주는 종료 조건

    left = []
    right = []
    pivot = lst.pop(0)

    for n in lst:
        if pivot > n:
            left.append(n)
        else:
            right.append(n)
    return quickSort(left) + [pivot] + quickSort(right)

ans = quickSort(q_lst)
print(*ans, sep='\n')
