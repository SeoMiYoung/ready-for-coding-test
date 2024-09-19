array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i # 제일 작은 값을 가리킴 (일단은 i값으로 세팅)

    # i+1 부터 인덱스 len(array)-1 까지 돌며, 가장 작은 값 찾기
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    
    # swap
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)

