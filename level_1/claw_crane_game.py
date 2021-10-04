#크레인 인형뽑기 게임

def solution(board, moves):
    stack = [] #stack 초기화
    answer = 0 #answer 초기화
    
    for m in moves: #moves를 도는 반복문
        for i in range(len(board)): #board를 도는 반복문
            if board[i][m-1]!=0: #해당하는 칸에 인형이 있다면
                stack.append(board[i][m-1]) #stack에 해당 숫자 추가
                board[i][m-1]=0 #0으로 초기화
                break #반복문 빠져나오기
                
        if len(stack)>=2 and (stack[-1]==stack[-2]): #stack에 2개의 원소 이상 존재하고, 위의 2개가 값이 같은 경우
            answer+=2 #answer에 삭제되는 인형의 갯수 추가
            stack.pop(-1) #인형 삭제
            stack.pop(-1) #인형 삭제

    return answer