change = 1260 # 거슬러줘야하는 금액
count = 0 # 발생하는 동전의 개수

# 알바생이 가지고 있는 돈 단위
moneyList = [500, 100, 50, 10]

for ml in moneyList:
    quotient = change // ml
    remainder = change % ml
    
    count = count + quotient
    change = remainder

print("동전의 총 개수: ", count)