#자릿수 더하기
#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    answer = list(map(int,str(n))) #입력받은 정수를 list형태로 변환
    answer = sum(answer) #list값의 합계
    return answer