import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().strip().split()

    if len(command) == 1:
        if command[0] == 'all':
            S = set([i for i in range(1, 21)])

        elif command[0] == 'empty':
            S = set()

    else:
        x, num = command[0], command[1]
        num = int(num)

        if x == 'add':
            S.add(num)
        elif x == 'remove':
            S.discard(num)
        elif x == 'toggle':
            if num in S:
                S.discard(num)
            else: S.add(num)

        elif x == 'check':
            if num in S:
                print(1)
            else:
                print(0)
