# 1, 2, 3 더하기 ( https://www.acmicpc.net/problem/9095 )
# input : 테스트 케이스 개수 T, 정수 n T개
import sys
input = sys.stdin.readline
T = int(input())
arr = [0] + [1] + [2] + [4] + [0] * 7

for i in range(4, 11):
    for j in range(i-3, i):
        arr[i] += arr[j]

for _ in range(T):
    n = int(input())
    print(arr[n])