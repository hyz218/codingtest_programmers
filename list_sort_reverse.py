#자연수 뒤집어 배열로 만들기
#자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 
#예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    answer = list(map(int,str(n))) #정수를 list 형태로 변환
    answer.reverse() #list 뒤집기
    return answer