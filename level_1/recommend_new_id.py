#신규 아이디 추천

import re

def solution(new_id):
    answer = ''
    answer = new_id.lower() #소문자 치환
    answer = re.sub('[^a-z\d\-\_\.]', '', answer) #소문자, 숫자, -, _, . 제외한 문자 제거 
    answer = re.sub('\.\.+','.',answer) #연속된 마침표 -> 하나의 마침표로 치환
    answer = re.sub('^\.|\.$', '', answer) #처음이나 끝에 위치한 마침표 제거
    if answer == '': #answer가 빈 문장이면 'a'대입
        answer = 'a'
    if len(answer)>=16: #길이가 16자 이상이면 앞쪽 15개 문자만 남기기
        answer = answer[:15]
    answer = re.sub('\.$', '', answer) #끝에 마친표 문자가 존재한다면 제거
    while len(answer) < 3: #문자가 3글자 이하라면 마지막 문자를 길이가 3이 될 때 까지 반복해서 붙이기
        answer += answer[-1:]
    
    
    return answer
