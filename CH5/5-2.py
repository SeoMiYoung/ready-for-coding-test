from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()


print(queue) # 출력: deque([3, 7, 1, 4])

# 역순으로 뒤집기
queue.reverse() 

# deque객체를 리스트 형태로 변환
print(list(queue)) # 출력: [4, 1, 7, 3]