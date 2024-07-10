# N, M 입력받음
N, M = map(int, input().split())
result = 0

for n in range(N):
    numList = list(map(int, input().split()))
    minNum = min(numList)

    if minNum > result:
        result = minNum


print(f'결과 출력: {result}')
