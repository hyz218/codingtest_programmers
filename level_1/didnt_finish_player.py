#완주하지 못한 선수
#수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

def solution(participant, completion):
    
    answer = [] #answer 초기화
    
    participant.sort() #participant 정렬
    completion.sort() #completion 정렬
    
    for p,c in zip(participant, completion):
        if (p != c): #참여자와 완주자가 다른 경우
            answer.append(p)
    if (answer == []): #answer가 업데이트 되지 않은 경우 
        answer.append(participant[-1])
    
    return answer[0]