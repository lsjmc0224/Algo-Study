rate = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

total = 0
result = 0

for _ in range(20):
    sub, hr, gra = input().split()
    hr = float(hr)
    if gra != 'P':
        total += hr
        result += hr * grade[rate.index(gra)]
print (result/total)       