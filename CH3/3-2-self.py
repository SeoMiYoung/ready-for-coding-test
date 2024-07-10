# 입력
# N M K
# 2 4 5 4 6

# split메서드는 기본적으로 공백을 기준으로 문자열을 나눠서 int형 type으로 list에 담아줌
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

# sort함수는 기본적으로 오름차순
data.sort() # [2, 4, 4, 5, 6]

first = data[N-1] # 가장 큰 수
second = data[N-2] # 두번째로 큰 수

sum = 0 # 합계

set_num = M // (K+1) # 세트 수
rest = M % (K+1) # 나머지
print(f'set_num: {set_num} rest: {rest}')

first_count = first*K*set_num + first*rest
second_count = second*set_num

sum = first_count + second_count
print(f'first_count: {first_count}')
print(f'second_count: {second_count}')
print(f'합계: {sum}')
