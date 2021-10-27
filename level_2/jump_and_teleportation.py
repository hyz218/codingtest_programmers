#점프와 순간이동

def solution(n):
    ans = 0 #ans 초기화
    
    while n>0: #n이 0보다 크면 계속 반복
        ans += n % 2 #점프를 해야하는 횟수 추가하기
        n //= 2

    return ans