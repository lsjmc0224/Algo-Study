# -2진수 ( https://www.acmicpc.net/problem/2089 )
# input 10진수
import sys
input = sys.stdin.readline

N = int(input())

# output =2진수
output = ''
if N == 0:
    output = '0'
else:
    while N != 0:
        if N % (-2) == 0:
            output += '0'
            N /= (-2)
        else:
            output += '1'
            N = (N - 1) / (-2)

print(output[::-1])
