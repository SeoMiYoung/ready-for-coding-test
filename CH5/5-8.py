def dfs(graph, v, visited):
    # 들어온 노드 방문처리
    visited[v] = 1
    # 방문한 노드 출력
    print(f'{v}', end=' ')

    # 인접한 노드 살펴보기
    for i in graph[v]:
        if visited[i]==0: # 아직 방문 전이라면
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [0] * 9

dfs(graph, 1, visited)