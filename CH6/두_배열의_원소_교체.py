N, K = map(int, input().split())
arrA = list(map(int, input().split())) #배열A
arrB = list(map(int, input().split())) #배열B

# 배열A의 가장 작은 원소랑, 배열B의 가장 큰 원소를 바꿔치기 해야함. 
### => 굳이 직접 찾을 필요가 과연 있을까...? NO
### => 배열A는 오름차순으로, 배열B는 내림차순으로 정렬해놓으면 그만이다.

arrA.sort() #오름차순
arrB.sort(reverse=True) #내림차순

for i in range(K):
    if arrA[i]<arrB[i]:
        arrA[i], arrB[i] = arrB[i], arrA[i]
    else:
        break # 더 이상 바꿀 필요가 없으므로, 반복문 탈출

# 최종 배열 A 원소의 합 출력
print(sum(arrA)) 