poly=input()
poly=poly.replace('XXXX','AAAA')  #변수 자체를 변형시키지 못한다
poly=poly.replace('XX','BB')
if 'X' in poly:
    print(-1)
else:
    print(poly)    
# replace 모듈 --> replace는 문자열을 변경하는 함수이다. 문자열 안에서 특정 문자를 새로운 문자로 변경하는 기능을 가지고 있다.
#  사용 방법은 '변수. replace(old, new, count)' 형식으로 사용한다.

# old : 현재 문자열에서 변경하고 싶은 문자

# new: 새로 바꿀 문자

# count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다. 


        






