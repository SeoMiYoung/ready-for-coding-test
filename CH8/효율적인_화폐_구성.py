N, M = map(int, input().split())
moneyList = [] # 화폐 단위 입력받기
countList = [10001] * (M+1)

for i in range(N):
    moneyList.append(int(input())) # moneyList: [3, 5, 7]

# 일단 0원에 세팅
countList[0] = 0

for i in moneyList: # 순서대로 3, 5, 7이 i에 할당됨
    for j in range(i, M+1):
        if countList[j-i] != 10001: #만약에 불가능한 값이 아니라면
            candidate = countList[j-i] + 1
            countList[j] = min(candidate, countList[j])

if countList[M] == 10001: #만약에 불가능한 값
    print(-1)
else:
    print(countList[M])
