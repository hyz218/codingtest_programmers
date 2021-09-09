#최대공약수와 최소공배수
#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
#배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

import math
def solution(n, m): #math 함수 이용
    answer = []
    
    max_num = math.gcd(n,m) #최대공약수
    answer.append(max_num)
    min_num = n*m / max_num #최소공배수
    answer.append(min_num)
    
    return answer

def solution_1(n, m):
    answer = []
    x=max(n,m) #x 자리에 큰 값 넣기
    y=min(n,m) #y 자리에 작은 값 넣기
    
    while y: #최대공약수 구하는 반복문
        x,y = y,x%y 
    answer.append(x)
    answer.append(n*m/x)
    
    return answer