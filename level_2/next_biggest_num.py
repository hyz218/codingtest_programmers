#다음 큰 숫자
#조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
#조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
#조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

def solution(n): 
    answer = 0 #answer 초기화
    binary_n = [] #n 이진변환 초기화
    
    m = n + 1 #m에 n보다 1큰 정수 저장
    
    while (n>=1): #n 이진화
        binary_n.append(n%2)
        n//=2
    binary_n.reverse()
    
    while(True):
        binary_m = [] #m의 이진수 변환 변수 초기화
        k=m #k에 m값 저장
        while (m>=1): #m 이진화
            binary_m.append(m%2)
            m//=2
        binary_m.reverse()
        if (binary_n.count(1)==binary_m.count(1)): #n과 m의 이진수에서 1의 갯수가 같을 경우
            break #반복문 종료
        else:
            m=k+1 #아닐 경우 1을 더해 다시 위의 과정 반복
        
    answer = k #answer에 k 대입
    return answer