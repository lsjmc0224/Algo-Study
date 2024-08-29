dir = ['E', 'W', 'S', 'N']
now = 3

for _ in range(10):
    command = int(input())
    if command == 1:  # 우향우
        if now == 0: now = 2
        elif now == 1: now = 3
        elif now == 2: now = 1
        else: now = 0
    elif command == 2:  # 뒤로 돌아
        if now == 0: now = 1
        elif now == 1: now = 0
        elif now == 2: now = 3
        else: now = 2
    elif command == 3:  # 좌향좌
        if now == 0: now = 3
        elif now == 1: now = 2
        elif now == 2: now = 0
        else: now = 1

print(dir[now])