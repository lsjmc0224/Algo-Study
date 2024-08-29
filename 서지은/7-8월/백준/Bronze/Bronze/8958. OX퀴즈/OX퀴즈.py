T = int(input())

for _ in range(T):
    n = 1
    total = 0
    quiz = list(map(str, input().strip()))

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            total += n
            n += 1
        else:
            n = 1
    print(total)