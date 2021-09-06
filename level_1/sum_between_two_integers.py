#두 정수 사이의 합
#두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
#예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

def solution(a, b): 
    answer = 0 #answer값 초기화
    if (a>b): #큰 수가 뒤로가게 하기 위해 두 값 비교 판별식
        a,b = b,a #swap
        
    for i in range(a,b+1,1):
        answer+=i #answer에 두 정수 사이의 값 더하기
    return answer