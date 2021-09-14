#이진 변환 반복하기

def solution(s):
    answer = [] #answer 초기화
    num_zero = 0 #제거한 0의 갯수
    j=0 #반복횟수
    
    while True:
        if s == "1": #문장이 1만 남으면 종료
            break
        j+=1 #반복 횟수 증가
        num_zero+=s.count('0') #0의 갯수 더하기
        s = s.replace('0','') #0 제거하기
        
        length = len(s) #남은 수의 길이
        new_num = []
        
        while length>=1: #2진 변환
            new_num.append(str(length%2))
            length//=2
        new_num = list(reversed(new_num))
        
        s = "".join(new_num) #list를 문자열로 변환

    answer.append(j) #반복횟수 answer에 추가
    answer.append(num_zero) #0의 갯수 answer에 추가
    return answer