#124 나라의 숫자
#124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용

def solution(n):
    answer = ''
    while n>0:
        if n%3 == 0:
            answer = '4'+answer
            n = n//3 -1
        else:
            answer = str(n%3) + answer
            n = n//3
        
    return answer