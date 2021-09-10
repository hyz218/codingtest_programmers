#3진법 뒤집기
#자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = [] #list 초기화
    num_of_three = 0 #삼진수 덧셈

    while (n>=1): #n이 1이 될 때까지 반복
        num = n%3 #3으로 나눈 나머지
        answer.append(str(num)) #나머지 answer list에 추가
        n=n//3 #n을 3으로 나누기

    answer.reverse() #3진수 뒤집기
    answer = "".join(answer) #리스트 합치기

    for i in range(len(answer)):
        if i==0: 
            num_of_three += int(answer[i])
        else:
            num_of_three += int(answer[i])*(3**i) #자릿수에 맞춰 3의 제곱 곱하기
    answer = num_of_three

    return answer