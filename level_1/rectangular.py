def solution(v):
    answer = []
    answer_x = []
    answer_y = []
    
    for i in range(len(v)):
        answer_x.append(v[i][0])
        answer_y.append(v[i][1])
    
    answer_x.sort()
    answer_y.sort()
    
    if answer_x[0]==answer_x[1]:
        answer.append(answer_x[2])
    else:
        answer.append(answer_x[0])
    
    if answer_y[0]==answer_y[1]:
        answer.append(answer_y[2])
    else:
        answer.append(answer_y[0])
    
    return answer