
N, K = map(int, input().split())

num = N
minCount = 0  # 연산 횟수

while True:
    if num==1:
        break
    
    if num%K == 0:
        num = num//K
        minCount = minCount + 1
    else:
        num = num - 1
        minCount = minCount + 1

print(f'출력: {minCount}')
