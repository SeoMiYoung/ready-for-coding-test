
num = int(input())
numList = list(map(int, input().split()))
sumTable = [0] * 4

sumTable[0] = numList[0]
sumTable[1] = max(sumTable[0], numList[1])

for i in range(2, len(numList)):
    # [first case] i를 터는 경우
    firstCase = sumTable[i-2] + numList[i]

    # [second case] i를 털지 않는 경우
    secondCase = sumTable[i-1]

    sumTable[i] = max(firstCase, secondCase)

# sumTable에는 현재 i위치에 왔을때 '처음~i위치'까지 고려해서 얻을 수 있는 경우 중 가장 큰 값이 i에 저장되어 있음
# 따라서 당연히 마지막 인덱스에 해당하는 값을 출력해야, 최댓값을 얻을 수 있음!
print(sumTable)
print(max(sumTable))
