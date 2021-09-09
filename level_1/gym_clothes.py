#체육복
#체육복을 도난당한 학생 존재. 여벌 체육복 있는 학생은 바로 앞번호의 학생이나 뒷번호의 학생에게만 체육복을 빌려줄 수 있음. 체육복을 빌려 체육수업을 들을 수 있는 학생의 최댓값 return

def solution(n, lost, reserve):
    answer = 0 #answer 초기화

    set_reserve = set(reserve) - set(lost) #여분의 체육복이 있는 학생 중 체육복을 도난 당한 학생 빼주기
    set_lost = set(lost) - set(reserve) #체육복을 도난당한 학생 중 여분 체육복이 있는 학생 빼주기
    
    for i in set_reserve: #여분 체육복이 있는 학생 반복문
        if (i-1 in set_lost):
            set_lost.remove(i-1) #앞번호 학생에게 체육복 빌려주기
        elif (i+1 in set_lost):
            set_lost.remove(i+1) #뒷번호 학생에게 체육복 빌려주기
    
    answer = n - len(set_lost) #학생수에서 체육수업을 못 받는 학생 수 빼주기
    
    return answer