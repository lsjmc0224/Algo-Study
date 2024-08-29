moeum = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while 1:
    word = input()
    cnt = 0

    if word == '#':
        break
    else:
        for i in range(len(word)):
            if word[i] in moeum:
                cnt += 1

        print(cnt)