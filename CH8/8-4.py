# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# 일단 정해진 건 없지만 크기를 100으로 두겠음
dpTable = [0] * 100

# 초기값은 일단 저장해놓기
dpTable[1] = 1
dpTable[2] = 1

# 반복문을 돌려가면 순차적으로 값 계산
for i in range(3, len(dpTable)):
    dpTable[i] = dpTable[i-1] + dpTable[i-2]

print(dpTable[len(dpTable)-1])  # 99번째 피보나치 값 출력
print(dpTable[6]) # 6번째 피보나치 값 출력