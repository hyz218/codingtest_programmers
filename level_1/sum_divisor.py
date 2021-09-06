#약수의 합
#정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

def solution(n):
    answer = 0
    for i in range(1,n+1): #0부터 시작하면 분모가 0이 되므로, 1부터 시작
        if (n%i==0): #i가 n의 약수이면 나머지가 0
            answer = answer+i #answer변수에 i 더하기
    return answer