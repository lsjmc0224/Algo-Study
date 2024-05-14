# 2진수 8진수 ( https://www.acmicpc.net/problem/1373 )
# input : 2진수 N
import sys
input = sys.stdin.readline
N = list(map(int, input().rstrip()))
stack = []
while N:
    temp = 0
    for i in range(3):
        if not N:
            temp += 0
        else: 
            temp += N.pop() * 2 ** i
    stack.append(str(temp))

print(''.join(stack[::-1]))