#로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = [] #answer 초기화
    
    num_zero = lottos.count(0) #알아 볼 수 없는 숫자의 갯수
    num_correct = 0 #당첨번호의 수 초기화
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            num_correct+=1 #번호가 당첨번호라면 당첨번호 추가
            
    answer.append(7-num_correct-num_zero) #최고순위(7등 - 당첨번호 - 당첨이 될 수 있는 번호의 수)
    answer.append(7-num_correct) #최저순위 (7등 - 당첨번호)
    
    if num_zero == 6: #모든 번호를 알아볼 수 없을 경우
        answer = [1,6]
    if num_zero == 0 and num_correct==0: #모든 번호를 알아볼 수 있으지만 당첨이 없는 경우
        answer = [6,6]
        
    return answer