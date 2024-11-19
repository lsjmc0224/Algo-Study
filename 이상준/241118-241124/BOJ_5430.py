# https://www.acmicpc.net/problem/5430 (AC)
from collections import deque

def AC(input_deque, p):
    is_forward = True
    return_deque = input_deque.copy()
    for calc in p:
        if calc == 'R':
            is_forward = not is_forward
        elif calc == 'D':
            if return_deque:
                if is_forward:
                    return_deque.popleft()
                else:
                    return_deque.pop()
            else: 
                return 'error', return_deque, is_forward
    return 'success', return_deque, is_forward

# input : T
T = int(input())
for _ in range(T):
    p = list(str(input()))
    n = int(input())
    input_str = input().strip()
    try:
        if input_str == "[]":
            numbers = []
        else:
            numbers = list(map(int, input_str.strip("[]").split(",")))
    except:
        print('error')
        continue
    
    input_deque = deque(numbers)
    state, return_deque, is_forward = AC(input_deque, p)
    
    if state == 'error':
        print('error')
    else:
        if is_forward:
            print("[" + ",".join(map(str, return_deque)) + "]")
        else:
            print("[" + ",".join(map(str, reversed(return_deque))) + "]")
