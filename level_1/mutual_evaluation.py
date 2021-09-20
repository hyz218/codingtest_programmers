#상호 평가
#만약, 학생들이 자기 자신을 평가한 점수가 유일한 최고점 또는 유일한 최저점이라면 그 점수는 제외하고 평균을 구합니다.

def solution(scores):
    answer = '' #answer 초기화
    
    for i in range(len(scores)):
        s=[] #s 초기화
        for j in range(len(scores[i])):
                s.append(scores[j][i]) #행으로 봐야하므로 j,i 추가
                
        if s[i] == min(s) and s.count(s[i]) == 1:
            del s[i] #s[i]가 최저값이면서 유일값이면 지우기
        elif s[i] == max(s) and s.count(s[i]) == 1:
            del s[i] #s[i]가 최댓값이면서 유일값이면 지우기
        
        num = sum(s)/len(s) #평균구하기
        
        if num>=90:
            answer = answer+'A'    
        elif num>=80:
            answer = answer+'B'
        elif num>=70:
            answer = answer+'C' 
        elif num>=50:
            answer = answer+'D' 
        else:
            answer = answer+'F'
            
    return answery