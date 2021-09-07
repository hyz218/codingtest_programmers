#콜라즈 추측
#1-1. 입력된 수가 짝수라면 2로 나눕니다. 
#1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
#2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

def solution(num):
    count = 0 #반복횟수 초기화
    answer = 0
    
    while True:
        if (num==1): #숫자가 1인지 판별
            answer = count
            break
            
        if (count==500): #횟수가 500번 시도했는지 판별
            answer = -1
            break
            
        if (num%2==0): #숫자가 짝수인지 판별
            num/=2 #짝수 일시 숫자를 2로 나누기
            count+=1 #횟수 증가
        else:
            num = num*3+1 #숫자가 홀수 일때, 숫자에 3을 곱하고 +1
            count+=1 #횟수 증가

    return answer