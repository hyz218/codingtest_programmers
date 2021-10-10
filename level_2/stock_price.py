# 주식가격
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

def solution(prices):
    answer = [] #answer 초기화
    
    for i in range(len(prices)): #prices list의 길이를 도는 반복문 설정
        cnt=0 #cnt=0으로 초기화
        for j in range(i,len(prices)-1): #i부터 (prices list의 길이-1)를 도는 반복문 설정
            if prices[i]<=prices[j]: #뒤의 주식가격이 높으면 cnt에 값 추가 
                cnt+=1
            else: #앞의 주식가격이 더 높은 경우 break
                break
        answer.append(cnt) #answer에 cnt값 추가
    return answer

def solution(prices):
    answer = [0]*len(prices) #answer 초기화
    stack = [] #stack 생성

    for i, price in enumerate(prices):
        #stack이 비었이면 false
        while stack and price < prices[stack[-1]]: #price가 더 작은 경우
            j = stack.pop() #stack에서 제거
            answer[j] = i - j #answer에 값 넣기
        stack.append(i) #stack에 i 삽입
        
    # for문 다 돌고 Stack에 남아있는 값들 pop
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
        
    return answer