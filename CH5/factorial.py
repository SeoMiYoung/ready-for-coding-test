def f(n):
    if n <= 1:
        print(f'종료')
        return 1
    
    print(f'현재 {n}! 이제 {n-1}!을 호출합니다!')
    print(f'{n}*{n-1}! 반환')
    return n * f(n-1)

f(6)