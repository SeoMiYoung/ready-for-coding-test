


# 부품이 최대 100,000까지 있을 수 있음
n = int(input())  # n: 5
totalItemInfo = [0] * 100000 # totalItemInfo: [0, 0, 0, 0, ......, 0, 0]
getItemInfo = list(map(int, input().split()))  # getItemInfo: [8, 3, 7, 9, 2]
for i in getItemInfo:
    totalItemInfo[i] = 1 # 존재하면 1표시

# print(f"totalItemInfo 출력: {totalItemInfo}")

findItemNum = int(input())  # findItemNum: 3
getFindItemInfo = list(map(int, input().split())) # getFindItemInfo: [5, 7, 9]
for j in getFindItemInfo:
    if totalItemInfo[j] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')