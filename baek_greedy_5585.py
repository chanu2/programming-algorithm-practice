number=0
change=[500,100,50,10,5,1]
price=1000-int(input())
for i in change:
    if price>=i:
        number+=price//i   
        price=price%i
print(number)