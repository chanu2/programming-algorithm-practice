import sys
n,m=map(int,sys.stdin.readline().split())
dic={}    # 딕션어리 선언
key1=[]    
value1=[]  
for i in range(n):
    a,b=(sys.stdin.readline().split())
    key1.append(a)
    value1.append(b)
for j in range(n):
    dic[key1[j]]=value1[j]     # key 값과 value값을 딕션어리에 저장 한다.
for _ in range(m):
    find_data=sys.stdin.readline().strip()   
    print(dic[find_data])     # 출력




# 조금 더 간단한 코드


# n, m = map(int, sys.stdin.readline().split())
# site = dict() # 딕셔너리형


# for _ in range(n):
#     id, pw = map(str, sys.stdin.readline().split())
#     site[id] = pw


# for _ in range(m):
#     address = str(sys.stdin.readline().rstrip())
#     print(site[address])    