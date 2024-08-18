# 매직스타 ( https://www.acmicpc.net/problem/3967 )

inp_arr = [0, 0,1,9,4,0,0,0,0,0,0,0,0]
not_in_star_arr = [2,3,5,6,7,8,10,11,12]


def permute_and_print_bool(arr, l, r):
    if l == r:
        return magic_inp_arr(arr[:])  # arr[:]로 배열을 복사하여 전달
    else:
        for i in range(l, r+1):
            arr[l], arr[i] = arr[i], arr[l]  # 위치 바꾸기
            result = permute_and_print_bool(arr, l + 1, r)
            if result != 'no':
                return result
            arr[l], arr[i] = arr[i], arr[l]  # 백트래킹

def magic_inp_arr(not_in_star_arr):
    temp_inp_arr = inp_arr[:]  # inp_arr 복사본을 사용
    temp_arr = not_in_star_arr[:]  # not_in_star_arr 복사본을 사용
    for i in range(len(temp_inp_arr) - 1, 0, -1):
        if temp_inp_arr[i] == 0:
            temp_inp_arr[i] = temp_arr.pop()
        else:
            continue
    print(temp_inp_arr)

    if is_it_twentysix(temp_inp_arr):
        return temp_inp_arr
    else:
        return False

def is_it_twentysix(inp_arr):
    return (
        inp_arr[1] + inp_arr[3] + inp_arr[6] + inp_arr[8] == 26 and
        inp_arr[1] + inp_arr[4] + inp_arr[7] + inp_arr[11] == 26 and
        inp_arr[2] + inp_arr[3] + inp_arr[4] + inp_arr[5] == 26 and
        inp_arr[2] + inp_arr[6] + inp_arr[9] + inp_arr[12] == 26 and
        inp_arr[5] + inp_arr[7] + inp_arr[10] + inp_arr[12] == 26 and
        inp_arr[8] + inp_arr[9] + inp_arr[10] + inp_arr[11] == 26
    )

result = permute_and_print_bool(not_in_star_arr, 0, len(not_in_star_arr) - 1)
print(result)