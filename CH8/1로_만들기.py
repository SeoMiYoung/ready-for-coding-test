

countTable = [0] * 30001 # DP 테이블 생성
inputNum = int(input()) # 숫자 입력

for i in range(2, inputNum + 1):
    calculateCount = 0

    # 1을 뺀 경우 --> 일단 초기 세팅해놓고
    countTable[i] = countTable[i-1] + 1

    # 지금부터 계속 기존에 세팅된 값을 업데이트 하면서 비교함
    # 만약 2로 나눴을 경우
    if inputNum % 2 == 0:
        # 둘 중에 더 작은 값을 할당(최소)
        countTable[i] = min(countTable[i], countTable[inputNum // 2] + 1)
    
    # 만약 3으로 나눴을 경우
    if inputNum % 3 == 0:
        # 둘 중에 더 작은 값을 할당(최소)
        countTable[i] = min(countTable[i], countTable[inputNum // 3] + 1)
    
    # 만약 5로 나눴을 경우
    if inputNum % 5 == 0:
        # 둘 중에 더 작은 값을 할당(최소)
        countTable[i] = min(countTable[i], countTable[inputNum // 5] + 1)

print(countTable[inputNum])
