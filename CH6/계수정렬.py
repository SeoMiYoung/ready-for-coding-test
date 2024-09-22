# 정렬하고자 하는 모든 원소의 값이 0보다 크거나 같다고 가정함
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언
countNum = [0] * (max(array)+1)  # 총 10칸의 count 공간이 만들어짐

for i in range(len(array)):  # 0~14
    countNum[array[i]] += 1

for i in range(max(array)+1): # 0~9
    for j in range(countNum[i]):
        print(i, end=' ')

