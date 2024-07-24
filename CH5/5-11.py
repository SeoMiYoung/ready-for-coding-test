from collections import deque

# N, M을 공백을 기준으로 구분하여 입력받기
N, M = map(int, input().split())

# 2차원 리스트 정보
miro_map = []
for mm in range(N):
    miro_map.append(list(map(int, input().split())))

# 위치 정보 (상, 하, 좌, 우)
dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

def bfs(n, m):
    # 일단 큐에 넣는다
    queue = deque()
    queue.append((n,m))

    while queue:
        # 일단 pop하고 시작함
        n, m = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치를 확인한다
        for d in range(4):
            new_n = n + dn[d]
            new_m = m + dm[d]

            # 만약 공간을 벗어나면
            if new_n<0 or new_n>=N or new_m<0 or new_m>=M:
                continue

            # 공간을 벗어나지 않음 + 막힘(0)
            if miro_map[new_n][new_m]==0:
                continue

            # 공간을 벗어나지 않음 + 갈 수 있음(1)
            if miro_map[new_n][new_m]==1:
                miro_map[new_n][new_m] = miro_map[n][m] + 1
                # 새로운 좌표 갔으니깐, 들렸다는 의미로 append
                queue.append((new_n, new_m))
    
    # while문이 끝남 == queue가 빔
    # 결과 출력
    print(miro_map) # 최종결과 출력해보기
    return miro_map[N-1][M-1]

# BFS 결과
result = bfs(0, 0)
print(f'bfs 결과: {result}')