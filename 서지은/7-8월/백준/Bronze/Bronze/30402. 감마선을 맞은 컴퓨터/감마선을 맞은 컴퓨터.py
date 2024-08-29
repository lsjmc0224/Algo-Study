# w는 춘배, b는 나비, g는 영철

pixel = [list(map(str, input().split())) for _ in range(15)]
cat = ''
for lst in pixel:
    for n in lst:
        if n == 'w':
            cat = 'chunbae'
        elif n == 'b':
            cat = 'nabi'
        elif n == 'g':
            cat = 'yeongcheol'
        else: continue
print(cat)