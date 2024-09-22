def findTarget(start, end, target, numList):
    while start <= end:
        # mid 계산
        mid = (start + end) // 2

        if numList[mid] == target: # target을 발견한 경우
            return mid+1
        elif numList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    # while문을 통해서 target을 찾지 못한 경우
    return None

        
num, target = list(map(int, input().split())) # num, target: [10, 7]
numList = list(map(int, input().split())) # numList: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

positionOfTarget = findTarget(0, num-1, target, numList)
if positionOfTarget == None:
    print("원소가 존재하지 않습니다.")
else:
    print(f"{positionOfTarget}")
    
