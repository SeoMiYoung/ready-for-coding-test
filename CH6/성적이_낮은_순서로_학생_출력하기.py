numOfStu = int(input())
studentList = []

for i in range(numOfStu):
    studentInfo = input().split() # ["홍길동", "95"]
    studentList.append((studentInfo[0], int(studentInfo[1]))) # [("홍길동", 95)]

# 성적을 기준으로 오름차순
list1 = sorted(studentList, key=lambda x: x[1])

# 성적을 기준으로 내림차순
list2 = sorted(studentList, key=lambda x: x[1], reverse=True)

# for i in range(numOfStu):
#     print(list1[i][0], end=' ')

# for i in range(numOfStu):
#     print(list2[i][0], end=' ')

### ------------------- 'for in 이름'과 'for in range(n)'는 다르다 ------------------------ ###
for i in list1:  
    print(i[0], end=' ')

for i in list2:
    print(i[0], end=' ')    