from collections import deque

def bfs(graph, v, visited):
    # 큐 생성
    queue = deque([v])
    # 방문 처리
    visited[v] = 1

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 원소 제거
        poped_v = queue.popleft()
        print(f'{poped_v}', end=' ')

        # poped_v와 연결된 원소들 큐에 넣기
        for i in graph[poped_v]:
            if visited[i]==0:
                queue.append(i)
                visited[i] = 1

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

visited = [0]*9

bfs(graph, 1, visited)