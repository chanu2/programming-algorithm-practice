def solution(nums):
    from itertools import combinations
    answer=0
    for i in combinations(nums,3):
        count=0
        divisor=sum(i)
        for j in range(1,divisor+1):
            if divisor % j==0:
                count+=1
        if count==2:
            answer+=1
    return answer

