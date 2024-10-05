# 메모이제이션
memoArr = [0] * 100  # memoArr: [0, 0, 0, 0, 0, ... , 0]



def calculateFibo(x):
    if x == 1 or x == 2:
        return 1
    
    if memoArr[x] == 0:  # 한번도 계산되지 않은 값이라면
        # 일단 새로운 값을 저장함
        memoArr[x] = calculateFibo(x-1) + calculateFibo(x-2)
        
    return memoArr[x]

print(calculateFibo(8))