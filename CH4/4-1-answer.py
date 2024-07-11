import time

# N을 입력받기
n = int(input())

# 좌표
x, y = 1, 1

# 계획
plans = input().split() 

start_time = time.time()

# 방향에 따른 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = ( x + dx[i] )
            ny = ( y + dy[i] )

    # 공간을 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    # 이동수행
    x, y = nx, ny

end_time = time.time()

execution_time = end_time - start_time

print(x,y)
print(f'걸린 시간: {execution_time}')