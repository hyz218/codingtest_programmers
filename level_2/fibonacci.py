def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    while n>=2:
        return fibonacci(n-1)+fibonacci(n-2)

def solution_2(n): #시간초과
    answer = 0
    answer = fibonacci(n)%1234567
    return answer

def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a%1234567