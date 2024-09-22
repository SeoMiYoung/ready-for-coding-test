def getMaxHeight(start, end, arr, goalOfSum):
    # 이전 mid 저장
    mid = 0
    resultMid = 0

    while start <= end:
        # mid 설정
        # beforeMid = mid
        mid = (start+end)//2

        # 떡 길이 합해보기
        sumOfLen = 0
        for s in range(len(lengthInfo)):
            if lengthInfo[s] >= mid:
                sumOfLen = sumOfLen + (lengthInfo[s] - mid)
        
        if sumOfLen > goalOfSum:
            resultMid = mid # 가장 그나마 조건에 만족하는 길이 저장 (딱 resultMid = mid가 안되는 경우도 있기 때문)
            start = mid + 1
        elif sumOfLen < goalOfSum:
            end = mid - 1
        else:
            resultMid = mid
            return mid
    
    return resultMid


numOfTteok, goalOfSum = list(map(int, input().split())) # numOfTteok: 4, goalOfSum: 6
lengthInfo = list(map(int, input().split()))  # lengthInfo: [19, 15, 10, 17]

# 떡중에 가장 길이가 긴 떡?
maxLen = max(lengthInfo)
# 배열
arr = [0]*(maxLen+1) # 총 길이가 20 (0~19)

print(getMaxHeight(1, maxLen, arr, goalOfSum))



