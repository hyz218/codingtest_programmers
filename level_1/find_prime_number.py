#소수 찾기
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

def solution_1(n): #비효율 코드
    answer = 0 #answer 초기화
    count = 0 #약수의 갯수인 count 초기화
    
    for i in range(2,n+1): #2부터 n까지의 반복문
        for j in range(1,i+1): #i의 약수의 갯수를 찾기 위한 반복문
            if i%j==0: #j가 i의 약수 여부 판별식
                count+=1 
        if count==2: #j가 소수이면 answer 갯수 추가
            answer+=1
        count=0 #count 초기화
    return answer

def solution(n):
    answer = 0 #answer 초기화
    num=set(range(2,n+1)) # 2부터 n+1까지의 집합

    for i in range(2,n+1): # 2부터 n까지 반복문
        if i in num: # 만약 i가 num에 존재하는지 판단
            num-=set(range(2*i,n+1,i)) # i의 배수는 num 집합에서 제외
    
    answer = len(num)
    return answer