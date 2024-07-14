'''
다음의  함수는 정수 배열에서 빠진숫자를 찾는다. 즉 배열은 0부터 배열 길이만큼의 모든 정수를 포함해야 하는데 숫자 하나가 빠져있다.
예를 들어 배열 [5,2,4,1,0]에는 숫자 3이 빠졌고 배열 [9,3,2,5,6,7,1,0,4]에는 8이 빠졌다.
다음은 O(N^2)짜리 구현이다.(includes 메서드를 사용하면 컴퓨터가 전체 배열에서 n을 찾아야하므로 그것만 이미 O(N)이다.)

function findMissingNumber(Array) {
    for(let i = 0; i < array.length; i++) {
        if(!array.includes(i)) {
            return i
        }
    }
    return null
}
'''
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    right = [x for x in array if x > pivot]
    middle = [x for x in array if x == pivot]
    left = [x for x in array if x < pivot]

    return quick_sort(left) + middle + quick_sort(right)

def find_missing_number(array):
    if len(array) == 0:
        return None
    for i in range(1, len(array) + 2):
        try: 
            if array[i - 1] != i:
                return i
        except IndexError:
                return i
        
        

array = [1,2,3,4,5]
print(find_missing_number(quick_sort(array)))