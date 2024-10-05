# dp방식(바텀업 방식, 반복)

num = int(input())

countTable = [0] * num

for i in range(0, num):
    if i==0:
        countTable[i] = 1
    elif i==1:
        countTable[i] = 3
    else:
        firstCase = countTable[i-1]
        secondCase = countTable[i-2] * 2
        totalCase = firstCase + secondCase
        countTable[i] = totalCase

print(countTable[num-1] % 796796)