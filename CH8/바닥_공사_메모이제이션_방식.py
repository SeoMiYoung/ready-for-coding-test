# memoization 방식 (탑다운, 재귀)

num = int(input())
countTable = [0] * num


# 탑다운
def topDown(n):
    if n == 0:
        return 1
    
    if n == 1:
        return 3
    
    # 값이 이미 계산되었는지 체크
    if countTable[n] != 0:
        return countTable[n]
    else:
        # 인덱스가 2부터인 경우
        firstCase = topDown(n-1)
        secondCase = topDown(n-2) * 2
        countTable[n] = (firstCase + secondCase) % 796796
        return countTable[n]

print(topDown(num-1))