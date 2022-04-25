import sys
T=int(sys.stdin.readline())   
inputr=[]
sequence=[0,0,1]
for _ in range(T):
    inputr.append(int(sys.stdin.readline()))
n=max(inputr)
for i in range(n):
    sequence.append((sequence[i+2]+sequence[i+1]+sequence[i])%1000000009)    
for j in inputr:
    print(sequence[j+2])
