da = 0
po = 0

N = int(input())

while True:
    cnt = 0
    for _ in range(N):
        expect = input()
        if expect == 'D':
            da += 1
        else:
            po += 1

        if da >= po + 2 or po >= da + 2:
            print(f"{da}:{po}")
            cnt = 1
            break

    if cnt == 0:
        print(f"{da}:{po}")
        break
    break