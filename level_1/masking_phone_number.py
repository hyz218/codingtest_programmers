#핸드폰 번호 가리기
#프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
#전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

def solution(phone_number):
    answer_1 = '*'*(len(phone_number)-4) # 마스킹하는 부분 문자열
    answer_2 = phone_number[len(phone_number)-4:len(phone_number)] #뒷번호 4자리만 남기기
    return answer_1+answer_2 #anwer_1과 answer_2 를 합쳐서 return