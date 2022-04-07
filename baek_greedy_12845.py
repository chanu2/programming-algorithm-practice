import sys
padding=[]
sum=0
n=int(sys.stdin.readline())
card=list(map(int,sys.stdin.readline().split()))
card.sort(reverse=True)  # 내림차순 정렬

if len(card)==1:
    print(0)
    exit()
for i in range(1,len(card)):
    sum+=card[0]+card[i]

print(sum)

   





