# import sys
# n=int(sys.stdin.readline())
# sum=0
# number=[int(input()) for _ in range(n)]
# number.sort()
# sum=0
# for i in range(1,len(number)):
#     sum+=number[0]
#     for j in range(1,i+1):
#         sum+=number[j]
# print(sum)
import sys
n=int(sys.stdin.readline())
number=[int(input()) for _ in range(n)]
number.sort()
sum=0
if len(number)==1:
    print(number[0])

else:
    j=len(number)-1
    sum+=number[0]*j
    for i in range(1,len(number)):
        sum+=number[i]*j
        j-=1
    print(sum)  