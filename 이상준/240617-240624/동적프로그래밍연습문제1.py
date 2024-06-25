'''
다음의 함수는 수 배열을 받아 그 합을 반환하되 합이 100을 초과하게 만드는 수는 제외한다. 
어떤 수를 더해 합이 100이 넘으면 그수는 무시한다. 
하지만 함수에서 불필요한 재귀 호출이 일어나고 있다. 
코드를 수정해 불필요한 재귀를 없애자

<코드>
def add_until_100(array):
    return 0 if array.length == 0
    if array[0] + add_until_100(array[1, array.length - 1]) > 100:
        return add_until_100(array[1, array.lenght - 1])
    else
        return array[0] + add_until_100(array[1, array.length - 1])
'''
arr = [61,54,55,55,55]

def add_until_100(array):
    if len(array) == 0:
        return 0
    ret = [0] * len(array)
    ret[0] = array[0]
    for i in range(1, len(array)):
        ret[i] = ret[i-1] + array[i]
        if ret[i] > 100:
            ret[i] = ret[i-1]
    return max(ret)

print(add_until_100(arr))

'''불필요한 재귀를 없앴다.'''