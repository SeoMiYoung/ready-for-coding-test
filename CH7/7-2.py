#######################################################
# 현재 재귀적으로 호출되는 구조를 띔 -> start, mid, end
#######################################################


def findTarget(start, end, target, numArray):
    # 재귀 구조에서 필수적인 종료조건!
    if start > end:
        return None
    
    # 중간점 계산
    mid = (start + end) // 2

    if numArray[mid] == target: # 만약에 mid값이 타겟이라면
        return mid+1
    elif numArray[mid] > target:
        return findTarget(start, mid-1, target, numArray)
    else: # numArray[mid] < target
        return findTarget(mid+1, end, target, numArray)
    

num, target = list(map(int, input().split())) # num, target = [10, 7]
numArray = list(map(int, input().split())) # numArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

positionOfTarget = findTarget(0, num-1, target, numArray)

# 출력
if positionOfTarget == None:
    print("원소가 존재하지 않습니다.")
else:
    print(f"{positionOfTarget}")