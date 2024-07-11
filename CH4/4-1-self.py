import time

N = int(input())
planner = input().split()  # 리스트로 담김

# 시작 시간 측정
start_time = time.time()

x = 1
y = 1

for i in range(len(planner)):
    plan = planner[i]  # 현재의 계획을 가져옴
    
    # 일단 이동
    if plan=='U':
        dy = y-1
        dx = x
    elif plan=='D':
        dy = y+1
        dx = x
    elif plan=='R':
        dy = y
        dx = x+1
    else:  # L인 경우
        dy = y
        dx = x-1
    
    # 범위 벗어낫나 확인
    if (dy!=0 and dx!=0 and dy!=N and dx!=N):  # 범위를 벗어나지 않았을 경우에만
        # 새로운 좌표 부여
        y = dy
        x = dx

# 종료시간 측정
end_time = time.time()

# 결과 출력
print(f'{dy} {dx}')
    
# 시간 출력
execution_time = end_time - start_time
print(f'걸린 시간: {execution_time}')
        

