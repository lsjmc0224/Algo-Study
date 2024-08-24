chess = [list(map(str, input().strip())) for _ in range(8)]
w = 'KPNBRQ'
b = 'kpnbrq'
white = {
    'K':0, 'P':1, 'N':3, 'B':3, 'R':5, 'Q':9
}
black = {
    'k':0, 'p':1, 'n':3, 'b':3, 'r':5, 'q':9
}

w_total, b_total = 0, 0

for lst in chess:
    for n in lst:
        if n == '.': continue
        elif n in w:
            w_total += white[n]
        elif n in b:
            b_total += black[n]

print(w_total-b_total)