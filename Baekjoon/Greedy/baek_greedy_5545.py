import sys
topping_calorie=[]
kind_topping=int(sys.stdin.readline())
dough_price,topping_price=map(int,sys.stdin.readline().split())
dough_calorie=int(sys.stdin.readline())
for _ in range(kind_topping):
    topping_calorie.append(int(sys.stdin.readline()))
topping_calorie.sort(reverse=True)  # 내림차순 정렬
result=dough_calorie/dough_price   # 토핑을 추가하지 않았을 떄

for i in range(1,kind_topping+1):
    calorie=sum(topping_calorie[0:i])+dough_calorie   #리스트 안의 수를 원하는 곳 까지 더하는 코드
    price=dough_price+(topping_price*i)
    if result<calorie/price:  # 비교를 통해서 result값을 변형하고 비교하는 코드
        result=calorie/price
    else:
        break
print(int(result))      # 소수점을 제거하고 출력  

            