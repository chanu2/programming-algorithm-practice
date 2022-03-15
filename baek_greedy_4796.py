import sys
cnt=0
L,P,V=map(int,sys.stdin.readline().split())
while L!=0 and P!=0 and V!=0:
    if (V%P)>=L:
        result=(V//P)*L+L
        cnt+=1
    else:
        result=(V//P)*L+(V%P)    
        cnt+=1
        
    print("Case %d: %d"%(cnt,result)) 
    L,P,V=map(int,sys.stdin.readline().split())

    
