#JadenCase 문자열 만들기

def solution(s):
    jaden = list(map(str,s.split(' '))) #문자를 list로 쪼개기

    for j in range(len(jaden)):
        jaden[j] = jaden[j].capitalize() #첫 글자만 대문자로 바꾸고 나머지 글자는 소문자로 바꾸는 내장함수 capitalize 사용 
    answer = ' '.join(jaden) #list를 문자열로 합쳐주기
    return answer