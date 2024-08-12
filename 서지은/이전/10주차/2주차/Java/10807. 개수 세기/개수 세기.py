import sys
input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
v = int(input())

print(list.count(v))