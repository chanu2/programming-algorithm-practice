s=list(map(int,input()))
result=''
n=s.count(0)
m=s.count(1)
s.reverse()
for _ in range(n//2):
    s.remove(0)
s.reverse()
for _ in range(m//2):
    s.remove(1)
for i in range(len(s)):

    result+=str(s[i])
print(result)


