#문자열 다루기 기본
#문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
#예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def solution(s):
    
    if (len(s)==4 or len(s)==6): #문장 길이가 4 혹은 6인지 판별
        if (s.isdigit() == True): #문장이 모두 숫자로 구성되어있는지 판별하는 함수
            return True  # True 반환
        
    return False #조건에 해당하지 않으면 False 반환