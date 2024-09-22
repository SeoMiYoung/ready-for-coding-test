
N = int(input())
N_set = set(map(int, input().split()))

M = int(input())
M_list = list(map(int, input().split()))

for i in range(M):
    if M_list[i] in N_set:
        print("yes", end=' ')
    else:
        print("no", end=' ')