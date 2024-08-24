T = int(input())
temp = T

minute = temp // 60
temp -= minute * 60
C = temp // 10

A = minute // 5
B = minute - A

if (A*300) + (B*60) + (C*10) != T:
    print(-1)

else: print(A, B, C)