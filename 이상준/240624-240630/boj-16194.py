# 카드 구매하기 ( https://www.acmicpc.net/problem/16194 )
#input N, P_1 ~ p_Ns
import sys
input = sys.stdin.readline
N = int(input())
card_price = [0] + list(map(int, input().split()))

#가장 작은 수 계사나기
def lowest_price(N, card_price):
    dp_array = card_price
    for i in range(2, N + 1):
        for j in range(0, i):
            # print(f'i = {i}, j = {j}')
            dp_array[i] = min(dp_array[i], dp_array[i - j] + dp_array[j])
    return dp_array[-1]
    # print(dp_array)

# print(card_price)
# print(N)
print(lowest_price(N, card_price))