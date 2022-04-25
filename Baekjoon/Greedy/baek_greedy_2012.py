import sys
n=int(sys.stdin.readline())
ranking=[]
fixranking=[]
satisfaction=0
for i in range(n):
    ranking.append(int(sys.stdin.readline()))
    fixranking.append(i+1)   
ranking.sort() #오름차순 정렬
for i in range(n):
    satisfaction+=abs(ranking[i]-fixranking[i])    #절대값을 구하는 코드

print(satisfaction) 
