from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_num_in_range(arr, start, end):
    left_index = bisect_left(arr, start)
    right_index = bisect_right(arr, end)
    return right_index - left_index
    

# 배열 선언
arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_num_in_range(arr, 4, 4))
print(count_num_in_range(arr, -1, 3))