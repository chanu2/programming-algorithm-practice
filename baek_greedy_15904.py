import sys

word=sys.stdin.readline()
UCPC=['U','C','P','C']
i=0
for s in UCPC:
    if s in word:
        i+=1
        word=word[(word.index(s)+1):]
        
    else:
        print("I hate UCPC")
        break
if i==4:
    print("I love UCPC")





                




        
