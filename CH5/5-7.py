# [[], [], []]
## 인덱스0의 list -> 0과 인접한 정보들 저장
## 인덱스1의 list -> 1과 인접한 정보들 저장
## 인덱스2의 list -> 2와 인접한 정보들 저장
graph = [[] for _ in range(3)] 

# 노드0과 인접한 정보들 저장
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드1과 인접한 정보들 저장
graph[1].append((0, 7))

# 노드2와 인접한 정보들 저장
graph[2].append((0, 5))

print(graph)