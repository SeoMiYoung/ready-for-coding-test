# N*M
N, M = map(int, input().split())

# 그래프 채우기
ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input().split())))

# DFS
def dfs(n, m):
    # 범위를 벗어남 => 아이스크림 공간이 없다는 의미
    if n<0 or n>=N or m<0 or m>=M:
        return False
    
    # 이미 방문한 칸
    if ice_map[n][m]==1:
        return False
    
    # 아직 방문을 하지 않은 칸
    if ice_map[n][m]==0:
        # 방문 처리
        ice_map[n][m] = 1

        # 상/하/좌/우 이동
        dfs(n-1, m)
        dfs(n+1, m)
        dfs(n, m-1)
        dfs(n, m+1)

        # 방문하지 않은 노드가 하나라도 있다는 의미는 아이스크림 하나 존재
        return True

# 입력
ice_count = 0
for n in range(N):
    for m in range(M):
        result = dfs(n, m)

        if result==True:
            ice_count += 1

print(f'총 아이스크림 개수: {ice_count}')