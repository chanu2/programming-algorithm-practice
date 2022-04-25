id_list=["muzi", "frodo", "apeach", "neo"]
report=["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list,report,k):
    report_list={name:[] for name in id_list}
    report=set(report)
    for i in report:
        r=i.split(' ')
        report_list[r[1]].append(r[0])# 딕션어리 리스트 안에 신고를 한사람을 넣는다.
    answer=[0 for _ in range(len(id_list))]    
    for j in id_list:
        if len(report_list[j])>=k:
            for p in report_list[j]:
                answer[id_list.index(p)]+=1
    return answer            

                      
print(solution(id_list,report,2))

