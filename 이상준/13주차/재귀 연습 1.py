'''
문자열 배열을 받아 모든 문자열에 쓰인 문자 개수를 반환하는 함수를 재귀적으로 작성하라
'''

# input : 배열
import sys
input = sys.stdin.readline
arr = list(map(str, input().split()))

# 모든 문자열에 쓰인 문자 개수를 반환
def function(arr, i = 0):
    if i >= len(arr) - 1:
        return len(arr[i])
    else:
        return len(arr[i]) + function(arr = arr, i = i + 1)

print(function(arr))
