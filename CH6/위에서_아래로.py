

n = int(input()) # n번의 입력 예정
n_list = [] # n개의 숫자를 담을 배열

for i in range(n):
    n_list.append(int(input()))

# 내림차순 정렬
## sorted()는 새로운 리스트 만들어냄
n_list = sorted(n_list, reverse=True)

for i in range(n):
    print(n_list[i], end=' ')

