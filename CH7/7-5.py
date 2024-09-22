# findNum - 이진탐색 함수
def findNum(target, itemIdList, start, end):
    # 종료 조건
    if start > end:
        return None
    
    # mid 구하기
    mid = (start + end) // 2

    if itemIdList[mid] == target:
        return mid+1
    elif itemIdList[mid] < target:
        return findNum(target, itemIdList, mid+1, end)
    else:
        return findNum(target, itemIdList, start, mid-1)
    
# N개의 부품 번호가 무엇인가요
N = int(input())  # N: 5
itemIdList = list(map(int, input().split()))  # itemIdList: [8, 3, 7, 9, 2]

# num개의 부품을 찾나요
num = int(input()) # num: 3
findNumList = list(map(int, input().split()))  # findNumList: [5, 7, 9]

# 이진 탐색을 하기 위해, itemIdList를 오름차순 정렬 시키기
itemIdList.sort() # 원본 변경, itemIdList: [2, 3, 7, 8, 9]

# 이진 탐색
for i in range(num):  # i: 0~2
    getPosition = findNum(findNumList[i], itemIdList, 0, N-1)
    # print(getPosition)

    if getPosition == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

