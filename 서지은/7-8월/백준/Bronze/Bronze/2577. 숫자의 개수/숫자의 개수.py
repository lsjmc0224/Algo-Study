A = int(input())
B = int(input())
C = int(input())

num = A*B*C
num = list(map(int, str(num)))
cnts = [0]*10

for i in range(10):
    if i in num:
        cnts[i] += num.count(i)

for n in cnts:
    print(n, sep='\n')