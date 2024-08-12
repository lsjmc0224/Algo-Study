A = int(input())
B = int(input())
C = int(input())
lst = [0]*10

mul = A*B*C
mult = [int(digit) for digit in str(mul)]

for n in mult:
    lst[n] += 1

for n in lst:
    print(n)