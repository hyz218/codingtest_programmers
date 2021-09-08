#이상한 문자 만들기
#문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

def solution(s):
    sentence = s.split(' ') #문장을 단어 단위로 쪼개기
    answer = '' #answer 초기화
    
    for i in range(len(sentence)):  #단어 갯수에 대한 반복문
        for j in range(len(sentence[i])): #단어 길이에 대한 반복문
            if j%2==0: #index가 짝수인지 판별
                answer = answer + sentence[i][j].upper() #대문자로 변환하여 answer에 추가
            else:
                answer = answer + sentence[i][j].lower() #소문자로 변환하여 answer에 추가
        if i < len(sentence)-1:
            answer = answer + ' ' #단어 사이의 공백 추가
        
    return answer