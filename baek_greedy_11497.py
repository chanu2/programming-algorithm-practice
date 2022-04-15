import sys
T=int(sys.stdin.readline())
for _ in range(T):

    n=int(sys.stdin.readline())
    tree=list(map(int,sys.stdin.readline().split()))
    tree.sort(reverse=True)
    result=[]
    max=0
    for i in range(len(tree)):
        if i%2==0:
            result.insert(0,tree[i])
        else:
            result.append(tree[i])              
    for i in range(len(result)-1):
        if max < abs(result[i]-result[i+1]):
            max = abs(result[i]-result[i+1])
    print(max)            
