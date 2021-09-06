#약수의 개수와 덧셈
#두 정수 left와 right가 매개변수로 주어집니다. 
#left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

def solution(left, right):
    answer = 0 #answer 초기화
    
    for i in range(left,right+1): #left부터 right까지 반복문
        num_divisor = 0 #약수의 갯수 초기화
        for j in range(1,i+1): #약수의 갯수를 파악하기 위한 반복문
            if (i%j==0): #j가 i의 약수인지 판별
                num_divisor +=1 #j가 i의 약수인 경우 약수의 갯수 증가
        if (num_divisor%2==0): #약수의 갯수가 짝수인 경우
            answer+=i #answer에 숫자 더하기
        else: #약수의 갯수가 홀수인 경우
            answer-=i #answer에 숫자 빼기
            
    return answer