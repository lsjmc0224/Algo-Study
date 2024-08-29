for _ in range(3):
    yoot = list(map(int, input().split()))
    a = yoot.count(0)
    b = yoot.count(1)

    if a == 1 and b == 3:
        print('A')
    elif a == 2 and b == 2:
        print('B')
    elif a == 3 and b == 1:
        print('C')
    elif a == 4: print('D')
    elif b == 4: print('E')