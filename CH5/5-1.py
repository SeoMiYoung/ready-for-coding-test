stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

# 최하위 원소부터 출력
print(stack)

# 최상위 원소부터 출력
print(stack[::-1])