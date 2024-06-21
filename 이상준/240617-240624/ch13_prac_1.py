'''
속도를 높이는 재귀 알고리즘 1

양수 배열이 주어졌을 때, 세 수의 가장 큰 곱을 반환하는 함수를 작성하라.
단, 퀵정렬을 사용해라 O(NlogN) 이 되도록
'''
class Array:
    def __init__(self, array):
        self.array = array
    
    def max_multiply(self):
        if len(self.array) == 0 or len(self.array) == 1:
            return None
        
        self.quicksort(0, len(self.array) - 1)
        return self.array[-1] * self.array[-2] * self.array[-3]

    def partition(self, left_pointer, right_pointer):
        pivot_index = right_pointer
        pivot = self.array[pivot_index]
        right_pointer -= 1
        
        while True:
            while self.array[left_pointer] < pivot:
                left_pointer += 1
            while self.array[right_pointer] > pivot:
                right_pointer -= 1
            if left_pointer >= right_pointer:
                break
            else:
                self.array[left_pointer], self.array[right_pointer] = self.array[right_pointer], self.array[left_pointer]
                left_pointer += 1
                right_pointer -= 1
        
        self.array[left_pointer], self.array[pivot_index] = self.array[pivot_index], self.array[left_pointer]
        return left_pointer
        
    def quicksort(self, left_index, right_index):
        if right_index - left_index <= 0:
            return
        pivot_index = self.partition(left_index, right_index)
        self.quicksort(left_index, pivot_index - 1)
        self.quicksort(pivot_index + 1, right_index)

# 배열의 예시
arr = [10, 3, 5, 6, 2, 8]

# Array 클래스의 인스턴스 생성
array_instance = Array(arr)

# 최대 곱 구하기
result = array_instance.max_multiply()

# 결과 출력
print(f"The maximum multiplication of the two largest numbers is: {result}")