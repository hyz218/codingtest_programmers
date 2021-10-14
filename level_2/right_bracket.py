#올바른 괄호
#'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    answer = True
    stack = [] #stack 구현
    
    for i in s: #문자를 도는 반복문 구현
        if i=='(': #i가 여는 괄호일 때
            stack.append(i) #list에 추가
        else: #i==')', i가 닫는 괄호일 때
            if stack and stack.pop() == '(': #pop한 값이 '('이고 stack이 비어있지않다면 반복문 다시 돌기
                continue
            else: #괄호가 맞지 않는 경우
                answer = False
                break
    if stack!=[]: #반복문을 다 돈 후, stack이 비어있지 않은 경우 False
        answer = False
    
    return answer