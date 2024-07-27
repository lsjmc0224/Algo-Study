lst = list(range(1, 31))

for _ in range(28):
    n = int(input())
    lst.remove(n)

for n in lst:
    print(n)