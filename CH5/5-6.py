INF = 999999999 # 무한의 비용 선언 (987654321로 선언하기도 함)

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)