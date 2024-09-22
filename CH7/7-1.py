def findTarget(num, target, nameArray):
    for i in range(num):
        if nameArray[i] == target: # 타겟과 일치한다면
            return i+1 # 인덱스 번호 + 1 값 반환 후 자동 함수 탈출

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
userInput = input().split() # input: ["5", "Dongbin"]
num = int(userInput[0]) # num: 5
target = userInput[1] # target: "Dongbin"

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
# nameArray: ["Hanul", "Jonggu", "Dongbin", "Taeil", "Sangwook"]
nameArray = input().split()

# 함수에 넘겨주기
PositionOfTarget = findTarget(num, target, nameArray) # findTarget(5, "Dongbin", ["Hanul", "Jonggu", ... ])
print(PositionOfTarget)
        

