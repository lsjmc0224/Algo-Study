N, M = map(int, input().split())
basket = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for n in basket:
    print(n, end=" ")