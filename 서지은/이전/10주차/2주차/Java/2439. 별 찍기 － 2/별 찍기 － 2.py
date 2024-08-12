import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    print(('*'*i).rjust(n))
    #가운데 정렬은 center, 왼쪽 정렬은 ljust
