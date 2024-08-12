lst = [int(input()) for _ in range(9)]
lst.sort()

sm = sum(lst)
one = two = 0

for i in range(9):
    for j in range(i+1, 9):
        # 9C7 = 9C2니까 배열 돌면서 2개를 뺐을 때 100이 되는 주솟값을 찾아서 
        # one, two에 넣어줌
        if sm-(lst[j]+lst[i]) == 100:
            one, two = lst[i], lst[j]
            break
#그리고 배열에서 없애기
lst.remove(one)
lst.remove(two)

for i in lst:
    print(i)