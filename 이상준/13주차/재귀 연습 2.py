'''
수 배열을 받아 짝수만 포함하는 새 배열을 반환하는 함수를 재귀적으로 작성하라.
'''

# input 수 배열
import sys
input = sys.stdin.readline
arr = list(map(int, input().split()))
print(arr)
output = []

# 짝수만 반환하는 함수
def function(arr, output, i = 0):
    if i >= len(arr):
        return output
    if arr[i] % 2 == 0:
        output.append(arr[i])
    return function(arr = arr, output = output, i = i + 1)

print(function(arr, output))