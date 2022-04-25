word=input()
croatia=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in croatia:
    word=word.replace(i,'*')   # replace 함수 --> A.replace('변형 할 문자열','무엇으로 변형할지 ','count// 만약 안적으면 자동으로 count-=1')
    #print(word)               # word.replace(i,'*')으로하면 변수 자체를 변형시키지는 않기때문에 오류가 발생한다.

print(len(word))




