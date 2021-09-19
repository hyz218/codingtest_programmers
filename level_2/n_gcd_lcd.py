#N개의 최소공배수
#이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

def gcd(a,b): #최대공약수 함수 구현
    if(a%b==0):
        return b
    else:
        return gcd(b,a%b)
    
def lcd(a,b): #최소공배수 함수 구현
    return (a*b) / gcd(max(a,b),min(a,b))

def solution(arr):
    answer = 1 #answer 초기화
    
    for num in arr: #arr전체를 도는 반복문
        answer = lcd(answer,num)
    
    return answer