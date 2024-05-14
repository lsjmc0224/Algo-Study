# Base Conversion ( https://www.acmicpc.net/problem/11576 )
# input : A, B 진법
import sys
input = sys.stdin.readline
A, B = map(int, input().split())

# input : m자리
m = int(input())

# input : A진법의 m자리 수
arr = list(map(int, input().split()))[::-1]

# A진법을 10진법으로
temp_10 = 0
for i in range(len(arr)):
    temp_10 = temp_10 + arr[i] * (A**i)

# 10진법을 B진법으로
res = []
while temp_10 != 0:
    res.append(str(temp_10 % B))
    temp_10 //= B

print(" ".join(res[::-1]))