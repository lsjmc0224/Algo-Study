N = int(input())
for _ in range(N):
    a, b = map(str, input().split())

    if len(a) != len(b):
        print("Impossible")
        continue

    a = list(a)
    b = list(b)

    a.sort()
    b.sort()

    flag = True
    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break
        else:
            flag = True

    if flag:
        print("Possible")
    else: print("Impossible")